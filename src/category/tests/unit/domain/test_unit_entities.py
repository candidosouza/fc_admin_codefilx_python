import unittest

import unittest
from datetime import datetime
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

    def test_constructor(self):
        category = Category('Movie', 'Some description', True, datetime.now())
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)