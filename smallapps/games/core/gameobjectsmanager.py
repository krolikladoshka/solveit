from typing import Optional, OrderedDict as OrderedDictType, Iterable
from collections import OrderedDict

from smallapps.games.core.entity import Entity
from smallapps.games.core.singleton import singleton


@singleton
class GameObjectsManager(Entity):
    def __init__(self, world_entity: Entity = None):
        super().__init__('GameObjectsManager')
        self.world: Entity = world_entity

        self.object_groups: OrderedDictType[str, OrderedDictType[int, Entity]] = OrderedDict()
        self.managed_object_groups: OrderedDictType[str, OrderedDictType[int, Entity]] = OrderedDict()

    def get_group(self, group: str) -> Iterable[Entity]:
        return self.object_groups.get(group, OrderedDict()).values()

    def instantiate(self, entity: Entity, group: str = 'all', managed: bool = True):
        self.object_groups.setdefault(group, OrderedDict())[id(entity)] = entity
        self.managed_object_groups.setdefault(group, OrderedDict())
        if managed:
            self.managed_object_groups[group][id(entity)] = entity

    def remove_entity(self, entity: Entity, group: Optional[str] = None) -> Optional[Entity]:
        if group:
            entity = self.object_groups[group].pop(id(entity), None)
            if entity:
                self.managed_object_groups[group].pop(id(entity), None)
            return entity
        else:
            for group_name, group in self.object_groups.items():
                if id(entity) in group:
                    entity = group.pop(id(entity))
                    self.managed_object_groups[group_name].pop(id(entity))
                    return entity

    def destroy(self, entity: Entity, group: Optional[str] = None):
        entity = self.remove_entity(entity, group)
        if entity:
            entity.is_enabled = False

        del entity

    def update(self, delta_time: int):
        for group_name, group in list(self.managed_object_groups.items()):
            print(f'Updating group "{group_name}" with delta time: {delta_time}')

            try:
                for entity_id, entity in list(group.items()):
                    entity.update(delta_time)
            except RuntimeError as e:
                raise e

    def draw(self, screen):
        for group_name, group in list(self.managed_object_groups.items()):
            print(f'Drawing group "{group_name}"')

            for entity_id, entity in list(group.items()):
                entity.draw(screen)
