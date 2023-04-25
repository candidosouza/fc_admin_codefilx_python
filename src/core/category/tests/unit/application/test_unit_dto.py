# pylint: disable=unexpected-keyword-arg
from typing import Optional
import unittest

from datetime import datetime
from core.category.application.dto import CategoryOutput


class TestCategoryOutputUnit(unittest.TestCase):

    def test_fields(self):
        self.assertEqual(CategoryOutput.__annotations__, {
            'id': str,
            'name': str,
            'description': Optional[str],
            'is_active': Optional[bool],
            'created_at': datetime
        })
