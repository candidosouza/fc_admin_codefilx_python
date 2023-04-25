# pylint: disable=unexpected-keyword-arg

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from core.category.application.dto import CategoryOutput
from core.category.domain.entities import Category
from core.category.domain.repositories import CategoryRepository


@dataclass(slots=True, frozen=True)
class CreateCategoryUseCase:

    category_repository: CategoryRepository

    def execute(self, input_param: 'Input') -> 'Output':
        category = Category(
            name=input_param.name,
            description=input_param.description,
            is_active=input_param.is_active
        )
        self.category_repository.insert(category)
        return self.Output(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
            created_at=category.created_at
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        name: str
        description: Optional[str] = Category.get_fields('description').default
        is_active: Optional[bool] = Category.get_fields('is_active').default

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass



@dataclass(slots=True, frozen=True)
class GetCategoryUseCase:

    category_repository: CategoryRepository

    def execute(self, input_param: 'Input') -> 'Output':
        category = self.category_repository.find_by_id(input_param.id)
        return self.Output(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
            created_at=category.created_at
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        id: str

    @dataclass(slots=True, frozen=True)
    class Output(CategoryOutput):
        pass
