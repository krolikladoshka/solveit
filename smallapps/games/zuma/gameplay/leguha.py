import math
import random
from typing import Optional, Union

import pygame
from smallapps.games.core.entity import Component, Entity, PositionComponent, SpriteComponent, SpriteEntity
from smallapps.games.core.events import EventEmitter, BaseEvent
from smallapps.games.core.gameobjectsmanager import GameObjectsManager
from smallapps.games.core.inputmanager import MouseMotionEvent, MouseButtonUpEvent
from smallapps.games.zuma.managers.tilemanager import MainTile, Sprites


class MouseMotionComponent(Component):
    def __init__(self, entity: 'Entity'):
        super().__init__(entity)

        self.mouse_position = pygame.Vector2(0, 0)
        self.event_emitter: EventEmitter = EventEmitter()
        self.event_emitter.subscribe(
            MouseMotionEvent.event_type,
            self.set_mouse_position
        )

    def set_mouse_position(self, event: MouseMotionEvent):
        self.mouse_position = pygame.Vector2(event.position[0], event.position[1])

    def update(self, delta_time: int):
        position: PositionComponent = self.get_component(PositionComponent)
        direction = self.mouse_position - position.position
        position.angle = math.degrees(math.atan2(-direction.y, direction.x))
        # position.angle = position.position.angle_to(self.mouse_position)


class BallColorComponent(Component):
    def __init__(self, entity, color: Sprites):
        super(BallColorComponent, self).__init__(entity)

        self.add_component(SpriteComponent)

        self.tile_manager: MainTile = MainTile()
        self.color: Sprites = color
        self.set_color(color)

    def set_color(self, color: Optional[Sprites]):
        sprite_component: SpriteComponent = self.get_component(SpriteComponent)

        if color is None:
            sprite_component.set_tile(None)

            return

        assert color in Sprites.colors()

        sprite_component.set_tile(self.tile_manager.colors[color])
        self.color = color


class Ball(SpriteEntity):
    def __init__(self, name: str, color: Optional[Sprites] = None, parent: Optional['Entity'] = None):
        tile_manager = MainTile()

        super().__init__(name, parent, color and tile_manager.sprites[color])

        self.add_component(BallColorComponent, color)
        self.get_component(PositionComponent).scale = 1
        self.add_component(CircleBoundary, tile_manager.sprite_size_balls / 2)
        self.color = color


class ChargedBall(Ball):
    def __init__(self, color: Optional[Sprites] = None, parent: Optional['Entity'] = None):
        tile_manager = MainTile()

        super().__init__('ChargedBall', color and tile_manager.sprites[color], parent)

        position_component: PositionComponent = self.get_component(PositionComponent)
        position_component.angle = 90
        position_component.scale = 1
        position_component.position = pygame.Vector2(87 / 2, 0)


class NextChargedBall(SpriteEntity):
    def __init__(self, color: Optional[Sprites] = None, parent: Optional['Entity'] = None):
        tile_manager = MainTile()

        super().__init__('NextChargedBall', parent, color and tile_manager.sprites[color])

        self.add_component(BallColorComponent, color)

        position_component: PositionComponent = self.get_component(PositionComponent)
        position_component.scale *= 0.5
        position_component.angle = 90
        position_component.position = pygame.Vector2(-27, 0)


class ProjectileHitEvent(BaseEvent):
    event_type = 'ProjectileHitEvent'
    target: Entity

    def __init__(self, sender: Entity, target: Entity):
        super().__init__(sender)
        self.target = target


class ShotBallComponent(Component):
    def __init__(self, entity: 'Entity', direction: pygame.Vector2, velocity: float = 500, *args, **kwargs):
        super().__init__(entity, *args, **kwargs)

        self.objects_manager: GameObjectsManager = GameObjectsManager()
        self.event_emitter: EventEmitter = EventEmitter()

        self.velocity: pygame.Vector2 = direction * velocity

    def update(self, delta_time: int):
        boundary: CircleBoundary = self.get_component(CircleBoundary)

        for ball in self.objects_manager.get_group('pathballs'):
            if boundary.is_overlapping(ball):
                self.event_emitter.emit(ProjectileHitEvent(self.entity, ball))
                return
        position: PositionComponent = self.get_component(PositionComponent)
        position.position = position.position + self.velocity * delta_time / 1000




class LeguhaShootingComponent(Component):
    def __init__(self, entity: Entity, charged_ball_entity: ChargedBall, next_chargd_ball_entity: NextChargedBall):
        super().__init__(entity)
        self.event_emitter: EventEmitter = EventEmitter()
        self.event_emitter.subscribe(MouseButtonUpEvent.event_type, self.shoot)
        # self.event_emitter.subscribe(FastRechargeBonusEvent.event_type, self.fast_recharge_bonus)

        self.position_component: PositionComponent = self.get_component(PositionComponent)
        self.charged_ball: Optional[ChargedBall] = charged_ball_entity
        self.next_charged_ball: Optional[NextChargedBall] = next_chargd_ball_entity

        self.recharging: bool = False
        self.recharge_delay: int = 1000
        self.elapsed_time: int = 0
        self.previous_charged: Optional[Sprites] = None
        self.objects_manager: GameObjectsManager = GameObjectsManager()
        self.charge_first()
        self.elapsed_bonus = 0

    def fast_recharge_bonus(self, event):
        if self.recharging:
            self.charge()
            self.elapsed_time = 0
            self.recharging = False
        if event.bonus_start:
            self.recharge_delay = 50
        else:
            self.recharge_delay = 1000

    def charge_first(self):
        charged_sprite_component: BallColorComponent = self.charged_ball.get_component(BallColorComponent)
        next_charged_sprite_component: BallColorComponent = self.next_charged_ball.get_component(BallColorComponent)

        colors = list(Sprites.colors())
        color = random.choice(colors)
        colors.remove(color)
        next_color = random.choice(colors)
        charged_sprite_component.set_color(color)
        next_charged_sprite_component.set_color(next_color)

    def charge(self):
        charged_sprite_component: BallColorComponent = self.charged_ball.get_component(BallColorComponent)
        next_charged_sprite_component: BallColorComponent = self.next_charged_ball.get_component(BallColorComponent)

        charged_sprite_component.set_color(next_charged_sprite_component.color)

        next_color = random.choice(
            list(set(Sprites.colors()) - {self.previous_charged, charged_sprite_component.color})
        )
        next_charged_sprite_component.set_color(next_color)

    def shoot(self, event: MouseButtonUpEvent):
        if event.button != 1:
            return

        if self.recharging:
            return

        charged_sprite_component: BallColorComponent = self.charged_ball.get_component(BallColorComponent)
        self.previous_charged = charged_sprite_component.color
        charged_sprite_component.set_color(None)

        self.recharging = True

        self.create_projectile()

    def create_projectile(self):
        projectile = Ball('ProjectileBall', self.previous_charged)

        charged_ball_position: PositionComponent = self.charged_ball.get_component(PositionComponent)
        direction = pygame.Vector2(1, 0).rotate(-charged_ball_position.angle + 90)
        projectile.add_component(ShotBallComponent, direction)

        projectile_position: PositionComponent = projectile.get_component(PositionComponent)
        projectile_position.position = charged_ball_position.position
        projectile_position.angle = charged_ball_position.angle

        self.objects_manager.instantiate(projectile, 'projectiles')

    def update(self, delta_time: int):
        class Bonus:
            def __init__(self, start):
                self.bonus_start = start

        if self.recharging:
            self.elapsed_time += delta_time

            if self.elapsed_time > self.recharge_delay:
                self.charge()
                self.recharging = False
                self.elapsed_time = 0
        self.elapsed_bonus += delta_time
        if self.elapsed_bonus >= 5000:
            if self.recharge_delay < 1000:
                self.fast_recharge_bonus(Bonus(False))
            else:
                self.fast_recharge_bonus(Bonus(True))
            self.elapsed_bonus = 0


class CircleBoundary(Component):
    def __init__(self, entity: Entity, radius: float = 0, position: Optional[pygame.Vector2] = None, *args, **kwargs):
        super().__init__(entity, *args, **kwargs)

        self._center = position
        self.event_emitter: EventEmitter = EventEmitter()
        self.radius: float = radius

    @property
    def center(self) -> pygame.Vector2:
        if self._center:
            return self._center
        return self.get_component(PositionComponent).position

    def is_overlapping(self, other: Union[Entity, Component]) -> bool:
        other: CircleBoundary = other.get_component(CircleBoundary)
        if not other:
            return False

        return (other.radius + self.radius) ** 2 >= self.center.distance_squared_to(other.center)

    def is_overlapping_rect(self, rect):
        rect = pygame.rect.Rect(*rect)

        distance = self.center - pygame.Vector2(rect.center)
        distance.x = abs(distance.x)
        distance.y = abs(distance.y)
        if distance.x > (rect[2] / 2 + self.radius):
            return False
        if distance.y > (rect[3] / 2 + self.radius):
            return False
        if distance.x <= rect[2] / 2:
            return True
        if distance.y <= rect[3] / 2:
            return True

        corner = (distance.x - rect[2] / 2) ** 2 + (distance.y - rect[3] / 2) ** 2

        return corner <= self.radius * self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.center, self.radius, 1)


class Leguha(SpriteEntity):
    def __init__(self):
        tile_manager = MainTile()

        super().__init__('Leguha', tile=tile_manager.sprites[Sprites.frog])

        self.charged_ball: ChargedBall = ChargedBall(parent=self)
        self.next_charged_ball: NextChargedBall = NextChargedBall(parent=self)

        self.add_component(MouseMotionComponent)
        self.add_component(LeguhaShootingComponent, self.charged_ball, self.next_charged_ball)
        self.add_component(CircleBoundary, 106 / 2 * 1.5)
