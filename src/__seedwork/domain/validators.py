from dataclasses import dataclass
from typing import Any, Dict, Generic, List, TypeVar
from abc import ABC
import abc

from __seedwork.domain.exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value: Any, prop: str):
        return ValidatorRules(value, prop)

    def required(self) -> 'ValidatorRules':
        if self.value is None or self.value == '':
            raise ValidationException(f'The {self.prop} is required')
        return self

    def string(self) -> 'ValidatorRules':
        if self.value is not None and not isinstance(self.value, str):
            raise ValidationException(f'The {self.prop} must be a string')
        return self

    def max_length(self, max_length: int) -> 'ValidatorRules':
        if self.value is not None and len(self.value) > max_length:
            raise ValidationException(
                f'The {self.prop} must be less than {max_length} characters')
        return self

    def min_length(self, min_length: int) -> 'ValidatorRules':
        if self.value is not None and len(self.value) < min_length:
            raise ValidationException(
                f'The {self.prop} must be greater than {min_length} characters')
        return self

    def boolean(self) -> 'ValidatorRules':
        if self.value is not None and self.value is not True and self.value is not False:
            raise ValidationException(f'The {self.prop} must be a boolean')
        return self


ErrorFields = Dict[str, List[str]]
PropsValidated = TypeVar('PropsValidated')

@dataclass(slots=True)
class ValidatorFieldsInterface(ABC, Generic[PropsValidated]):
    errors: ErrorFields = None
    validated_data: PropsValidated = None

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError()
