import unittest
from rest_framework import serializers

from core.__seedwork.domain.validators import DRFValidator


class StubSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    name = serializers.CharField()
    price = serializers.CharField()


class TestDRFValidatorsIntegration(unittest.TestCase):
    def test_validation_with_error(self):
        validator = DRFValidator()
        serializer = StubSerializer(data={})
        is_valid = validator.validate(serializer)
        self.assertFalse(is_valid)
        self.assertEqual(validator.errors, {
                         'name': ['This field is required.'], 'price': ['This field is required.']})

    def test_validation_without_error(self):
        validator = DRFValidator()
        serializer = StubSerializer(data={'name': 'some value', 'price': 7})
        is_valid = validator.validate(serializer)
        self.assertTrue(is_valid)
        self.assertEqual(validator.validated_data, {
                         'name': 'some value', 'price': '7'})
