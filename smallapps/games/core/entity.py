import math
from typing import Dict, Type, Union, OrderedDict as OrderedDictType, Optional, List
from collections import OrderedDict

import numpy
import numpy as np
import pygame
from pygame.sprite import Sprite, Group

components: Dict[str, Type['Component']] = {}


def component_key(component_type: Union[Type['Component'], str]) -> str:
    if isinstance(component_type, str):
        return component_type
    return component_type.__name__


def component_type_by_name(name: Union[Type['Component'], str]) -> Type['Component']:
    assert name in components or name.__name__ in components

    if isinstance(name, type):
        return components[name.__name__]
    return components[name]


def get_component(entity: 'Entity', component_type: Union[Type['Component'], str]) -> Optional['Component']:
    assert isinstance(component_type, type) or isinstance(component_type, str)

    return entity.components.get(component_key(component_type))


def add_component(entity: 'Entity', component_type: Union[Type['Component'], str], *args, **kwargs) -> 'Component':
    component_type = component_type_by_name(component_type)

    component = component_type(entity, *args, **kwargs)
    entity.components[component_type.__name__] = component

    return component


def remove_component(entity: 'Entity', component_type: Union[Type['Component'], str]):
    assert isinstance(component_type, type) or isinstance(component_type, str)

    component_type = component_type_by_name(component_type)

    component = entity.components.pop(component_type.__name__, None)
    if component:
        del component


class ComponentMeta(type):
    def __new__(mcs, clsname, bases, attrs):
        component_type = super().__new__(mcs, clsname, bases, attrs)

        if clsname != 'Component':
            components[clsname] = component_type
        return component_type


class Component(metaclass=ComponentMeta):
    def __init__(self, entity: 'Entity', *args, **kwargs):
        self.entity: 'Entity' = entity
        self.is_enabled: bool = True

    def get_component(self, component_type: Union[Type['Component'], str]) -> 'Component':
        return self.entity.get_component(component_type)

    def add_component(self, component_type: Union[Type['Component'], str], *args, **kwargs) -> 'Component':
        return self.entity.add_component(component_type, *args, **kwargs)

    def remove_component(self, component_type: Union[Type['Component'], str]):
        return self.remove_component(component_type)

    def update(self, delta_time: int):
        pass

    def draw(self, screen):
        pass


class TransformComponent(Component):
    def __init__(self, entity: 'Entity'):
        super().__init__(entity)

        self.transform = numpy.identity(3, dtype=float)
        self.angle = 0
        self._scale = 1
        self.position = pygame.Vector2(0, 0)
        self.local_angle = 0
        self.local_position = pygame.Vector2(0, 0)
        self.local_scale = 1
        self.parent_transform: Optional[TransformComponent] = None
        if self.entity.parent:
            parent_transform: TransformComponent = self.entity.parent.get_component(TransformComponent)
            self.parent_transform = parent_transform

    @classmethod
    def identity(cls):
        return np.identity(3, dtype=float)

    @classmethod
    def rotation(cls, angle: float):
        cos = numpy.cos(angle)
        sin = numpy.sin(angle)

        matrix = cls.identity()
        matrix[0, 0] = cos
        matrix[0, 1] = sin
        matrix[1, 0] = -sin
        matrix[1, 1] = cos

        return matrix

    def transform_to_parent(self):
        parent_transform: TransformComponent = self.entity.parent.get_component(TransformComponent)

        return parent_transform.transform @ self.transform

    @classmethod
    def translation(cls, vector: pygame.Vector2):
        matrix = cls.identity()
        matrix[0, 2] = vector.x
        matrix[1, 2] = vector.y

        return matrix

    @classmethod
    def scaling(cls, scale: Union[pygame.Vector2, float]):
        matrix = identity()

        if isinstance(scale, pygame.Vector2):
            matrix[0, 0] = scale.x
            matrix[1, 1] = scale.y

            return matrix

        matrix[0, 0] = matrix[1, 1] = scale
        return matrix

    def rotate(self, angle: float):
        self.angle += angle
        rotation_matrix = self.rotation(math.radians(self.angle))

        self.transform = rotation_matrix @ self.transform

    def rotate_center(self, angle: float):
        self.angle += angle
        cos = numpy.cos(angle)
        sin = numpy.sin(angle)
        back = self.translation(-self.position)
        forth = self.translation(self.position)
        rotate = self.rotation(angle)
        self.transform = forth @ rotate @ back @ self.transform

    def set_rotation_center(self, angle: float):
        self.rotate_center(-self.angle)
        self.rotate_center(angle)
        self.angle = angle

    def translate(self, vector: pygame.Vector2):
        self.position += vector
        self.transform = self.translation(vector) @ self.transform
        # self.transform[0, 2] += vector.x
        # self.transform[1, 2] += vector.y

    def set_position(self, vector: pygame.Vector2):
        to_origin = self.translation(-self.position)
        self.position = vector
        self.transform = self.translation(self.position) @ to_origin @ self.transform

    def scale(self, scale: float):
        self._scale = scale
        scaling = self.scaling(scale)
        back = self.translation(-self.position)
        forth = self.translation(self.position)
        self.transform = forth @ scaling @ back @ self.transform

    def apply(self, point):
        point = np.array([point[0], point[1], 1], dtype=float)

        transform = self.transform
        if self.parent_transform:
            transform = self.parent_transform.transform @ transform
        dot = np.dot(transform, point)

        return dot[0], dot[1]


class PositionComponent(Component):
    def __init__(self, entity: 'Entity'):
        super().__init__(entity)

        self._position: pygame.Vector2 = pygame.Vector2(0, 0)
        self._angle: float = 0
        self._scale: float = 1

        if self.entity.parent:
            parent_position_component: PositionComponent = self.entity.parent.get_component(PositionComponent)
            self._position = pygame.Vector2(parent_position_component._position)
            self._angle = parent_position_component._angle
            self._scale = parent_position_component._scale

    def children_positions(self) -> List['PositionComponent']:
        children = []
        for child in self.entity.children.values():
            child_position = child.get_component(PositionComponent)
            children.append(child_position)

        return children

    @property
    def position(self) -> pygame.Vector2:
        return self._position

    @position.setter
    def position(self, vector: pygame.Vector2):
        offset = vector - self.position
        self._position = vector

        for child_position_component in self.children_positions():
            child_position_component.position = child_position_component.position + offset

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float):
        angle_offset = value - self.angle
        self._angle = value

        for child_position_component in self.children_positions():
            child_position_offset = child_position_component.position - self.position
            new_child_position = self.position + child_position_offset.rotate(-angle_offset)

            child_position_component.position = new_child_position
            child_position_component.angle += angle_offset

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float):
        offset = value / self._scale
        self._scale = value

        for child_position_component in self.children_positions():
            child_position_component.scale *= offset

    def distance(self, other: Union['Entity', 'Component']) -> float:
        return self.position.distance_to(other.get_component(PositionComponent).position)

    def distance_squared(self, other: Union['Entity', 'Component']) -> float:
        return self.position.distance_squared_to(other.get_component(PositionComponent).position)


class SpriteComponent(Component, Sprite):
    def __init__(self, entity: 'Entity'):
        super().__init__(entity)

        self.position_component: PositionComponent = self.add_component(PositionComponent)
        self.surface = None
        self.image = None
        self.rect: pygame.Rect = self.image.get_rect() if self.image else pygame.Rect(0, 0, 0, 0)

    def set_tile(self, tile: Optional[pygame.Surface]):
        if not tile:
            self.surface = tile
            self.image = tile
        else:
            self.surface = tile
            self.image, self.rect = self.transform(tile)

    def rotate(self, surface: pygame.Surface):
        result = pygame.transform.rotate(surface, self.position_component.angle)
        rect = result.get_rect(center=self.position_component.position)

        return result, rect

    def transform(self, surface: pygame.Surface):
        result = surface
        rect = surface.get_rect()
        rect.center = self.position_component.position

        if abs(self.position_component.angle) > 1e-6:
            result, rect = self.rotate(result)

        if abs(self.position_component.scale - 1) > 1e-6 or abs(self.position_component.scale - 1) != 0:
            size = self.position_component.scale * rect.width, self.position_component.scale * rect.height
            result = pygame.transform.smoothscale(result, size)
            rect = result.get_rect(center=rect.center)

        return result, rect

    def draw(self, screen: pygame.Surface):
        if not self.surface:
            return
        self.image, self.rect = self.transform(self.surface)
        screen.blit(self.image, self.rect)
        if __debug__:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class Entity:
    def __init__(self, name: str = '', parent: Optional['Entity'] = None):
        self._parent = None
        self.components: OrderedDictType[str, Component] = OrderedDict()
        self.name: str = name

        # self.add_component(TransformComponent)
        self.add_component(PositionComponent)

        self.children: OrderedDictType[int, 'Entity'] = OrderedDict()
        self.parent: Optional['Entity'] = parent
        self.is_enabled: bool = True

    @property
    def parent(self) -> Optional['Entity']:
        return self._parent

    @parent.setter
    def parent(self, value: Optional['Entity']):
        if self._parent:
            self._parent.children.pop(id(self), None)
        self._parent = value

        # transform: TransformComponent = self.get_component(TransformComponent)

        if value:
            value.children[id(self)] = self

            # parent_transform: TransformComponent = value.get_component(TransformComponent)
            # transform.parent_transform = parent_transform
            # transform.parent_transform = None

    def add_component(self, component_type: Union[Type[Component], str], *args, **kwargs) -> 'Component':
        return add_component(self, component_type, *args, **kwargs)

    def get_component(self, component_type: Union[Type[Component], str]) -> Optional[Component]:
        return get_component(self, component_type)

    def remove_component(self, component_type: Union[Type[Component], str]):
        return remove_component(self, component_type)

    def update(self, delta_time: int):
        if not self.is_enabled:
            return

        for component_name, component in self.components.items():
            if component.is_enabled:
                component.update(delta_time)
        for child in self.children.values():
            child.update(delta_time)

    def draw(self, screen):
        if not self.is_enabled:
            return

        for component in self.components.values():
            if component.is_enabled:
                component.draw(screen)

        for child in self.children.values():
            child.draw(screen)


class SpriteEntity(Entity):
    def __init__(self, name: str, parent: Optional['Entity'] = None, tile: Optional[pygame.Surface] = None):
        super().__init__(name, parent)

        self.add_component(PositionComponent)
        sprite_component: SpriteComponent = self.add_component(SpriteComponent)
        sprite_component.set_tile(tile)

    def draw(self, screen):
        super().draw(screen)