from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.entities import Entity
from __seedwork.domain.exceptions import NotFoundException


# ET = Entity Type
ET = TypeVar('ET', bound=Entity)


class RepositoryInterface(Generic[ET], ABC):
    @abstractmethod
    def insert(self, entity: ET) -> ET:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: ET) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError


# repository in memory
@dataclass(slots=True)
class InMemoryRepository(RepositoryInterface[ET], ABC):

    items: List[ET] = field(default_factory=lambda: [])

    def insert(self, entity: ET) -> ET:
        self.items.append(entity)

    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        return self._get(entity_id)

    def find_all(self) -> List[ET]:
        return self.items

    def update(self, entity: ET) -> None:
        entity_found = self._get(entity.id)
        index = self.items.index(entity_found)
        self.items[index] = entity

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        id_str = str(entity_id)
        entity_found = self._get(id_str)
        self.items.remove(entity_found)
    
    def _get(self, entity_id: str) -> ET:
        if entity := next(filter(lambda x: x.id == entity_id, self.items), None):
            return entity
        else:
            raise NotFoundException(f"Entity not found using ID '{entity_id}'")
