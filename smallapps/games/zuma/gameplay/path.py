import random
from functools import lru_cache
from typing import List, Tuple, Union, Optional

import pygame

from smallapps.games.core.entity import Component, Entity, PositionComponent
from smallapps.games.core.events import EventEmitter, BaseEvent
from smallapps.games.zuma.gameplay.leguha import CircleBoundary, Ball, ProjectileHitEvent, ShotBallComponent, \
    BallColorComponent
from smallapps.games.core.gameobjectsmanager import GameObjectsManager
from smallapps.games.zuma.managers.tilemanager import Sprites


class BezierPath:
    def __init__(self, width: float):
        self.points: List[pygame.Vector2] = []
        self.width: float = width

    @property
    @lru_cache
    def path_length(self) -> float:
        return sum(self.segment_approximated_length(i) for i in range(self.segments_count))

    @property
    def segments_count(self) -> int:
        return (len(self.points) - 4) // 3 + 1

    def path_from_points(self, anchors: List[pygame.Vector2]):
        p1, p2 = anchors[0], anchors[1]
        direction = p2 - p1
        self.points.extend([
            p1,
            p1 - pygame.Vector2(-1, 0) * direction.magnitude() / 4,
            p2 - pygame.Vector2(1, 0) * direction.magnitude() / 4,
            p2
        ])
        for i in range(2, len(anchors)):
            self.add_point(anchors[i])

    def add_point(self, anchor: pygame.Vector2):
        if self.points:
            next_control_point = self.points[-1] * 2 - self.points[-2]
            new_control_point = (next_control_point + anchor) / 2
            self.points.extend([
                next_control_point, new_control_point, anchor,
            ])
        else:
            self.points.extend([
                anchor + pygame.Vector2(-1, 0),
                anchor + (pygame.Vector2(-1, 0) + pygame.Vector2(0, -1)) / 2,
                anchor + (pygame.Vector2(1, 0) + pygame.Vector2(0, 1)) / 2,
                anchor + pygame.Vector2(1, 0),
            ])

    def get_normals(self, vector: pygame.Vector2) -> Tuple[pygame.Vector2, pygame.Vector2]:
        return pygame.Vector2(-vector.y, vector.x).normalize(), pygame.Vector2(vector.y, -vector.x).normalize()

    def get_width_normals(self, vector: pygame.Vector2) -> Tuple[pygame.Vector2, pygame.Vector2]:
        down, up = self.get_normals(vector)

        return down * self.width / 2, up * self.width / 2

    def get_segment_points(self, i: int) -> List[pygame.Vector2]:
        return self.points[i * 3:i * 3 + 4]

    @lru_cache(256)
    def get_point_on_segment(self, i: int, t: float):
        # assert 0 <= t <= 1

        segment_points = self.get_segment_points(i)

        return self.bezier_cubic_function(segment_points, t)

    @lru_cache
    def segment_approximated_length(self, i: int) -> float:
        steps = 10
        points = []

        t = 0
        while t < 1:
            point = self.get_point_on_segment(i, min(t, 1))
            points.append(point)
            t += 1 / steps

        length = 0
        for i in range(len(points) - 1):
            length += (points[i + 1] - points[i]).magnitude()

        return length

    @staticmethod
    def bezier_cubic_function(points: List[pygame.Vector2], t: float):
        t_squared = t * t
        t_cubed = t_squared * t
        mt = 1 - t
        mt_squared = mt * mt
        mt_cubed = mt_squared * mt
        result = (
                points[0] * mt_cubed +
                3 * points[1] * mt_squared * t +
                3 * points[2] * mt * t_squared +
                points[3] * t_cubed
        )

        return result

    @lru_cache
    def segment_derivative(self, segment: int, t: float) -> pygame.Vector2:
        segment_points = self.get_segment_points(segment)

        return self.bezier_derivative(tuple(segment_points), t)

    @staticmethod
    def bezier_derivative(points: Tuple[pygame.Vector2, ...], t: float) -> pygame.Vector2:
        try:
            return (
                    t * t * (3 * (points[3] - points[0]) + 9 * (points[1] - points[2])) +
                    t * (6 * (points[0] - 2 * points[1] + points[2])) +
                    3 * (points[1] - points[0])
            )
        except IndexError as e:
            raise e


class BezierDrawingComponent(Component):
    def __init__(self, entity: 'Entity', path: BezierPath):
        super().__init__(entity)
        self.path: BezierPath = path
        self.discreditized: int = 50

        self.precomputed_lines: List[pygame.Vector2] = []
        self.precompute_path()

    def precompute_path(self):
        step = 1 / 15
        for segment in range(self.path.segments_count):
            t = 0
            while t < 1:
                point = self.path.get_point_on_segment(segment, max(0, min(t, 1)))
                self.precomputed_lines.append(point)
                t += step

    def draw(self, screen):
        pygame.draw.lines(screen, (255, 0, 0), False, self.precomputed_lines, 2)


class BallReachedThePitEvent(BaseEvent):
    event_type = 'BallReachedThePitEvent'

    def __init__(self, sender: Entity):
        super().__init__(sender)
        self.left_balls_count: int = 0
        # self.left_balls_count: int = sender_component.active_balls_count


class BallBezierMovementComponent(Component):
    # TODO: ball movement looks ugly, probably because of wrong derivative calculation
    def __init__(self, entity: 'Entity', bezier_path: BezierPath, *args, **kwargs):
        super().__init__(entity, *args, **kwargs)
        self.current_length = 0
        self.ball_radius: float = self.get_component(CircleBoundary).radius
        self.bezier_path: BezierPath = bezier_path
        self.t = 0
        self.max_t: float = float(self.bezier_path.segments_count)
        # self.current_segment = 0

    @property
    def current_segment(self) -> int:
        return int(self.t)

    @property
    def local_parameter(self) -> float:
        return self.t - self.current_segment

    def move_along_path(self, distance: float):
        if self.current_segment >= self.bezier_path.segments_count:
            return
        generator: BallGeneratorComponent = self.entity.parent.get_component(BallGeneratorComponent)

        derivative = generator.bezier_path.segment_derivative(self.current_segment, self.local_parameter).magnitude()
        self.t += min(self.max_t, distance / derivative)

    def update(self, delta_time: float):
        generator: BallGeneratorComponent = self.entity.parent.get_component(BallGeneratorComponent)

        # self.current_segment += 1
        if self.current_segment >= generator.bezier_path.segments_count:
            # self.event_emitter.emit(BallReachedThePitEvent(self, self))

            return

        position_component: PositionComponent = self.get_component(PositionComponent)
        position_component.position = generator.bezier_path.get_point_on_segment(
            self.current_segment, min(self.local_parameter, 1)
        )
        self.move_along_path(generator.ball_radius * 2 * delta_time / 1000)


class BallGeneratorComponent(Component):
    def __init__(self, entity: 'Entity', bezier_path: BezierPath, *args, **kwargs):
        super().__init__(entity, *args, **kwargs)

        self.objects_manager: GameObjectsManager = GameObjectsManager()
        self.event_emitter: EventEmitter = EventEmitter()
        self.event_emitter.subscribe(ProjectileHitEvent.event_type, self.handle_hit)

        self.ball: Ball = None
        self.balls = []
        self.event_emitter: EventEmitter = EventEmitter()
        self.bezier_path: BezierPath = bezier_path

        # self.ball_radius: float = self.ball.get_component(CircleBoundary).radius
        self.ball_radius = 16
        self.total_balls_count: int = int(round(self.bezier_path.path_length / (self.ball_radius * 2)))
        self.total_spawned_balls: int = 0
        self.active_balls_count: int = 0
        self.elapsed = 0

        entrance_position = self.bezier_path.points[0]
        derivative = self.bezier_path.segment_derivative(0, 0)
        entrance_position += derivative.normalize() * self.ball_radius / 2
        self.entrance: Entity = Entity(name='entrance', parent=self.entity)
        self.entrance_trigger: CircleBoundary = self.entrance.add_component(
            CircleBoundary, self.ball_radius,
            # self.bezier_path.points[0],
            entrance_position
        )

        end_position = self.bezier_path.points[-1]
        derivative = self.bezier_path.segment_derivative(self.bezier_path.segments_count - 1, 1)
        end_position += -derivative.normalize() * self.ball_radius / 2
        self.end: Entity = Entity(name='end', parent=self.entity)
        self.end_trigger: CircleBoundary = self.end.add_component(
            CircleBoundary, self.ball_radius,
            # self.bezier_path.points[-1],
            end_position
        )
        self.end: Entity = Entity(name='end', parent=self.entity)

    def handle_hit(self, event: ProjectileHitEvent):
        other: BallBezierMovementComponent = event.target.get_component(BallBezierMovementComponent)
        target_position: int = self.balls.index(event.target)

        for i in range(target_position):
            self.balls[i].get_component(BallBezierMovementComponent).move_along_path(-self.ball_radius * 2)

        self.add_ball(event.sender, target_position)
        event.sender.get_component(PositionComponent).angle = 0
        new: BallBezierMovementComponent = event.sender.get_component(BallBezierMovementComponent)

        new.t = other.t
        # new.move_along_path(-self.ball_radius * 2)
        event.sender.remove_component(ShotBallComponent)

        # for ball in self.balls[target_position + 1:]:
        #     ball.get_component(BallBezierMovementComponent).move_along_path(self.ball_radius * 2)
        self.rearrange(target_position)

    def rearrange(self, inserted_ball_index: int):
        if len(self.balls) < 3:
            return

        def can_rearrange(idx):
            start, end = max(idx - 1, 0), min(idx + 1, len(self.balls))
            same_color_balls = 0
            while start >= 0:
                if get_color(idx) != get_color(start):
                    same_color_balls += 1
                    break
                start -= 1
            while end < len(self.balls):
                if get_color(idx) != get_color(end):
                    same_color_balls += 1
                    break
                end += 1
            return start + 1, end

        def get_color_entity(ball: Ball):
            return ball.get_component(BallColorComponent).color

        def get_color(idx: int):
            return get_color_entity(self.balls[idx])

        start, end = can_rearrange(inserted_ball_index)
        if abs(end - start) >= 3:
            for ball in range(start, end):
                self.objects_manager.destroy(self.balls[ball], 'pathballs')
                # self.balls.remove(ball)
            # removed_size = rightmost - leftmost
            idx = end
            for i in range(start, start + len(self.balls) - end):
                moving_component: BallBezierMovementComponent = self.balls[idx].get_component(
                    BallBezierMovementComponent)
                leftmost_moving: BallBezierMovementComponent = self.balls[i].get_component(
                    BallBezierMovementComponent
                )
                moving_component.t = leftmost_moving.t
                idx += 1
            self.balls = self.balls[:start] + self.balls[end:]

            # self.balls = self.balls[:leftmost] + self.balls[rightmost:]
            self.rearrange(min(start, len(self.balls) - 1))

    def add_ball(self, ball: Optional[Ball] = None, idx: Optional[int] = None):
        if not ball:
            colors = list(Sprites.colors())
            color = random.choice(colors)
            ball = Ball('', color, self.entity)
        else:
            ball.parent = self.entity
            self.objects_manager.remove_entity(ball, 'projectiles')
        ball.add_component(BallBezierMovementComponent, self.bezier_path)

        # self.entity.children[id(ball)] = ball
        self.objects_manager.instantiate(ball, 'pathballs', managed=False)
        if idx:
            self.balls.insert(idx, ball)
        else:
            self.balls.insert(0, ball)
            # self.balls = [ball] + self.balls
        self.total_spawned_balls += 1
        self.active_balls_count += 1

    def update(self, delta_time: int):
        # add circle boundary to start
        # if no circle inside that boundary then spawn
        # else do nothing

        if not self.balls:
            self.add_ball()
        if self.end_trigger.is_overlapping(self.balls[-1]):
            self.event_emitter.emit(BallReachedThePitEvent(self.entity))

            return
        if not self.entrance_trigger.is_overlapping(self.balls[0]):
            if self.total_spawned_balls < self.total_balls_count:
                self.add_ball()

    # def draw(self, screen):
    #     super().draw()


class NotSoRandomPath(Entity):
    def __init__(self,
                 n: int, m: int, block_width: float, block_height: float,
                 obstacles: List[Union[Entity, Component]] = None):
        super().__init__('', None)

        self.obstacles: List[CircleBoundary] = []
        if obstacles:
            self.obstacles = list(filter(None, [
                obstacle.get_component(CircleBoundary)
                for obstacle in obstacles
            ]))

        self.n = n
        self.m = m
        self.points: List[pygame.Vector2] = []
        self.width = 8
        self.block_width = block_width
        self.block_height = block_height

        path = self.construct_path(n, m, (n - 1, m - 1))
        self.discrete_path = path
        self.generate_points(path)

        self.bezier_path: BezierPath = BezierPath(30)
        self.bezier_path.path_from_points(self.points)

        self.add_component(BezierDrawingComponent, self.bezier_path)
        generator = self.add_component(BallGeneratorComponent, self.bezier_path)

    def generate_points(self, path: List[Tuple[int, int]]):
        self.points.append(
            pygame.Vector2(path[0][0] * self.block_width, path[0][0] * self.block_height)
        )
        for index in range(1, len(path)):
            i, j = path[index]
            y = i * self.block_height + self.block_height / 2
            x = j * self.block_width + self.block_width / 2
            # while True:
            #     center_x = j * block_width + block_width / 2
            #     center_y = i * block_height + block_height / 2
            #     x_lefttop = center_x - block_width / 4
            #     y_lefttop = center_y - block_height / 4
            #     x = random.uniform(x_lefttop, x_lefttop + block_width / 2)
            #     y = random.uniform(y_lefttop, y_lefttop + block_height / 2)
            #     # y = random.uniform(i * block_height + i * block_height / 2, i * block_height + block_height)
            #     # x = random.uniform(j * block_width / 2, j * block_width + block_width)
            #     if not self.points or pygame.Vector2(x, y) != self.points[-1]:
            #         break
            self.points.append(pygame.Vector2(x, y))

    def construct_path(self, n, m, end) -> list:
        visited = set()
        directions = [
            # down, up
            (1, 0), (-1, 0), (0, -1), (0, 1)
        ]
        r = []

        def is_overlapping_obstacles(i, j) -> bool:
            rect = (j * self.block_width, i * self.block_height, self.block_width, self.block_height)

            def is_overlapping_obstacle(obstacle: CircleBoundary) -> bool:
                return obstacle.is_overlapping_rect(rect)

            return any(map(is_overlapping_obstacle, self.obstacles))

        def can_step(i, j) -> bool:
            if i >= n or j >= m or j < 0 or i < 0:
                return False
            if is_overlapping_obstacles(i, j):
                visited.add((i, j))
            return (i, j) not in visited

        stack = [(0, 0, [])]
        while stack:
            i, j, result = stack.pop()
            if (i, j) == end:
                r = result + [(i, j)]

                break
            visited.add((i, j))
            possible_direction = []
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]

                if not can_step(next_i, next_j):
                    continue
                possible_direction.append((next_i, next_j))

            if possible_direction:
                random.shuffle(possible_direction)
                for next_i, next_j in possible_direction:
                    stack.append((next_i, next_j, result + [(i, j)]))
        return r

    def draw(self, screen):
        def get_normals(point: pygame.Vector2, point2) -> (pygame.Vector2, pygame.Vector2):
            # normal = pygame.Vector2(self.points[i].y, self.points[i].x).normalize() * self.width / 2
            direction = point2 - point
            # normal = pygame.Vector2(direction.y, direction.x).normalize() * self.width / 2
            up = point + pygame.Vector2(-direction.y, direction.x).normalize() * self.width / 2
            down = point + pygame.Vector2(direction.y, -direction.x).normalize() * self.width / 2
            return up, down

        # for i in range(len(self.points) - 1):
        #     up_i, down_i = get_normals(self.points[i], self.points[i + 1])
        #     direction = (self.points[i + 1] - self.points[i])
        #     up_i1 = up_i + direction
        #     down_i1 = down_i + direction
        #     # up_i1, down_i1 = get_normals(self.points[i + 1])
        #     pygame.draw.line(screen, (255, 255, 255), self.points[i], self.points[i + 1])
        #     pygame.draw.line(screen, (255, 0, 255), up_i, up_i1)
        #     pygame.draw.line(screen, (0, 255, 0), down_i, down_i1)
        for point in self.discrete_path:
            rect = pygame.rect.Rect(point[1] * self.block_width, point[0] * self.block_height, self.block_width,
                                    self.block_height)
            pygame.draw.rect(screen, (255, 0, 0), rect, 1)
        # self.get_component(BezierDrawingComponent).draw(screen)
        super().draw(screen)
