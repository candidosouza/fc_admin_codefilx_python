
import unittest
from datetime import timedelta
from django.utils import timezone
from core.category.domain.entities import Category
from core.category.infra.repositories import CategoryInMemoryRepository


class TestCategoryInMemoryRepositoryUnit(unittest.TestCase):
    repo: CategoryInMemoryRepository

    def setUp(self) -> None:
        self.repo = CategoryInMemoryRepository()

    def test_if_no_filter_when_filter_param_is_null(self):
        entity = Category(name='Movie')
        items = [entity]

        
        items_filtered = self.repo._apply_filter(items, None) # pylint: disable=protected-access
        self.assertListEqual(items_filtered, items)

    def test_filter(self):
        items = [
            Category(name='test'),
            Category(name='TEST'),
            Category(name='fake'),
        ]
        
        items_filtered = self.repo._apply_filter(items, 'TEST') # pylint: disable=protected-access
        self.assertListEqual(items_filtered, [items[0], items[1]])

    def test_sort_by_created_at_when_sort_param_is_null(self):
        items = [
            Category(name='test'),
            Category(name='TEST', created_at=timezone.now() +
                     timedelta(seconds=100)),
            Category(name='fake', created_at=timezone.now() +
                     timedelta(seconds=200)),
        ]
        
        items_filtered = self.repo._apply_sort(items, None, None) # pylint: disable=protected-access
        self.assertListEqual(items_filtered, [items[2], items[1], items[0]])

    def test_sort_by_name(self):
        items = [
            Category(name='cba'),
            Category(name='bcd'),
            Category(name='abc'),
        ]

        
        items_filtered = self.repo._apply_sort(items, "name", "asc") # pylint: disable=protected-access
        self.assertListEqual(items_filtered, [items[2], items[1], items[0]])

        
        items_filtered = self.repo._apply_sort(items, "name", "desc") # pylint: disable=protected-access
        self.assertListEqual(items_filtered, [items[0], items[1], items[2]])
