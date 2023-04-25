

from dataclasses import is_dataclass
from typing import Optional
import unittest
from unittest.mock import patch

from core.category.application.use_cases import CreateCategoryUseCase
from core.category.infra.repositories import CategoryInMemoryRepository
from core.category.domain.entities import Category


class TestCreateCategoryUseCaseUnit(unittest.TestCase):

    use_case: CreateCategoryUseCase
    category_repo: CategoryInMemoryRepository

    def setUp(self):
        self.category_repo = CategoryInMemoryRepository()
        self.use_case = CreateCategoryUseCase(self.category_repo)

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(CreateCategoryUseCase))

    def test_input(self):
        self.assertTrue(is_dataclass(CreateCategoryUseCase.Input))
        self.assertEqual(
            CreateCategoryUseCase.Input.__annotations__,
            {
                'name': str,
                'description': Optional[str],
                'is_active': Optional[bool],
            }
        )
        #pylint: disable=no-member
        description_field = CreateCategoryUseCase.Input.__dataclass_fields__[
            'description']
        self.assertEqual(description_field.default,
                         Category.get_fields('description').default)

        is_active_field = CreateCategoryUseCase.Input.__dataclass_fields__[
            'is_active']
        self.assertEqual(is_active_field.default,
                         Category.get_fields('is_active').default)

    def test_execute(self):
        with patch.object(
            self.category_repo,
            'insert',
            wraps=self.category_repo.insert
        ) as spy_insert:
            input_param = CreateCategoryUseCase.Input(name='Movie')
            output = self.use_case.execute(input_param)
            spy_insert.assert_called_once()
            self.assertEqual(output, CreateCategoryUseCase.Output(
                id=self.category_repo.items[0].id,
                name='Movie',
                description=None,
                is_active=True,
                created_at=self.category_repo.items[0].created_at
            ))

        input_param = CreateCategoryUseCase.Input(
            name='Movie',
            description='some description',
            is_active=False
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(output, CreateCategoryUseCase.Output(
            id=self.category_repo.items[1].id,
            name='Movie',
            description='some description',
            is_active=False,
            created_at=self.category_repo.items[1].created_at
        ))

        input_param = CreateCategoryUseCase.Input(
            name='Movie',
            description='some description',
            is_active=True
        )
        output = self.use_case.execute(input_param)
        self.assertEqual(output, CreateCategoryUseCase.Output(
            id=self.category_repo.items[2].id,
            name='Movie',
            description='some description',
            is_active=True,
            created_at=self.category_repo.items[2].created_at
        ))
