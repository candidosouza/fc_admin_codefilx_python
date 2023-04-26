from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import Any

from core.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId())  # pylint: disable=unnecessary-lambda

    @property
    def id(self):  # pylint: disable=invalid-name
        return str(self.unique_entity_id)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict['id'] = self.id
        return entity_dict

    @classmethod
    def get_fields(cls, entity_fields: str) -> field:
        return cls.__dataclass_fields__[entity_fields]  # pylint: disable=no-member
