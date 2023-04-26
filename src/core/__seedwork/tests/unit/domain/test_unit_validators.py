import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from dataclasses import fields
from rest_framework.serializers import Serializer
from rest_framework import serializers

from core.__seedwork.domain.validators import (
    ValidatorRules, ValidationException, ValidatorFieldsInterface, DRFValidator,
    StrictBooleanField, StrictCharField
)


class TestValidatorsRulesUnit(unittest.TestCase):

    def test_values_method(self):
        validator = ValidatorRules.values('some value', 'prop')
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, 'some value')
        self.assertEqual(validator.prop, 'prop')

    def test_required_rules(self):
        invalid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': '', 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).required()
            self.assertEqual(
                f'The {data["prop"]} is required',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': 'Some value', 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).required(),
                ValidatorRules
            )

    def test_string_rules(self):
        invalid_data = [
            {'value': 5, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).string()
            self.assertEqual(
                f'The {data["prop"]} must be a string',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': "some value", 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).string(),
                ValidatorRules
            )

    def test_max_length_rules(self):
        invalid_data = [
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).max_length(4)
            self.assertEqual(
                f'The {data["prop"]} must be less than 4 characters',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).max_length(5),
                ValidatorRules
            )

    def test_min_length_rules(self):
        invalid_data = [
            {'value': "x", 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:

                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).min_length(3)
            self.assertEqual(
                f'The {data["prop"]} must be greater than 3 characters',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).min_length(4),
                ValidatorRules
            )

    def test_bollean_rules(self):
        invalid_data = [
            {'value': "x", 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).boolean()
            self.assertEqual(
                f'The {data["prop"]} must be a boolean',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).boolean(),
                ValidatorRules
            )

    def test_throw_a_validation_exception_when_combine_two_or_more_rules(self):
        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                None, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop is required',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                5, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop must be a string',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                "x" * 6, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop must be less than 5 characters',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                "x" * 4, 'prop'
            ).required().string().min_length(5)
        self.assertEqual(
            'The prop must be greater than 5 characters',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                None, 'prop'
            ).required().boolean()
        self.assertEqual(
            'The prop is required',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                5, 'prop'
            ).required().boolean()
        self.assertEqual(
            'The prop must be a boolean',
            assert_rules.exception.args[0],
        )

    def test_valid_cases_for_combination_between_rules(self):
        ValidatorRules.values('test', 'prop').required().string()
        ValidatorRules.values(
            'x' * 5, 'prop').required().string().max_length(5)

        ValidatorRules.values(True, 'prop').required().boolean()
        ValidatorRules.values(False, 'prop').required().boolean()


class TestValidatorFieldsInsterfaceUnit(unittest.TestCase):
    def test_throw_error_when_validate_method_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            ValidatorFieldsInterface()  # pylint: disable=abstract-class-instantiated
        self.assertEqual(
            assert_error.exception.args[0],
            "Can't instantiate abstract class ValidatorFieldsInterface " +
            "with abstract method validate"
        )

    def test_sample(self):
        fields_class = fields(ValidatorFieldsInterface)
        errors_field = fields_class[0]
        self.assertEqual(errors_field.name, 'errors')
        self.assertIsNone(errors_field.default)

        validated_data_field = fields_class[1]
        self.assertEqual(validated_data_field.name, 'validated_data')
        self.assertIsNone(validated_data_field.default)


class TestDRFValidatorsUnit(unittest.TestCase):

    @patch.object(Serializer, 'is_valid', return_value=True)
    @patch.object(
        Serializer,
        'validated_data',
        return_value={'field': 'value'},
        new_callable=PropertyMock
    )
    def test_if_validated_data_is_set(
        self,
        mock_validated_data: PropertyMock,
        mock_is_valid: MagicMock
    ):
        validator = DRFValidator()
        is_valid = validator.validate(Serializer())
        self.assertTrue(is_valid)
        self.assertEqual(validator.validated_data, {'field': 'value'})
        mock_validated_data.assert_called()
        mock_is_valid.assert_called()

    @patch.object(Serializer, 'is_valid', return_value=False)
    @patch.object(
        Serializer,
        'errors',
        return_value={'field': ['some error']},
        new_callable=PropertyMock
    )
    def test_if_errors_is_set(self, mock_errors: PropertyMock, mock_is_valid: MagicMock):
        validator = DRFValidator()
        is_valid = validator.validate(Serializer())
        self.assertFalse(is_valid)
        self.assertEqual(validator.errors, {'field': ['some error']})
        mock_errors.assert_called()
        mock_is_valid.assert_called()


class TestStrictCharFieldUnit(unittest.TestCase):
    def test_if_is_valid_when_not_str_values(self):
        class StubStrictCharFieldSerializer(serializers.Serializer):  # pylint: disable=abstract-method
            name = StrictCharField()

        serializer = StubStrictCharFieldSerializer(data={'name': 7})
        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'name': [serializers.ErrorDetail(string='Not a valid string.', code='invalid')]
        })

    def test_none_value_is_valid(self):
        class StubStrictCharFieldSerializer(serializers.Serializer):  # pylint: disable=abstract-method
            name = StrictCharField(required=True, allow_null=True)

        serializer = StubStrictCharFieldSerializer(data={'name': None})
        self.assertTrue(serializer.is_valid())

    def test_is_valid(self):
        class StubStrictCharFieldSerializer(serializers.Serializer):  # pylint: disable=abstract-method
            name = StrictCharField(required=True, allow_null=True)

        serializer = StubStrictCharFieldSerializer(data={'name': 'some value'})
        serializer.is_valid()
        self.assertEqual(serializer.validated_data, {'name': 'some value'})


class TestStrictBolleanFieldUnit(unittest.TestCase):
    def test_if_is_valid_when_not_str_values(self):
        class StubStrictBolleanFieldSerializer(serializers.Serializer):  # pylint: disable=abstract-method
            active = StrictBooleanField()

        message_error = 'Must be a valid boolean.'

        serializer = StubStrictBolleanFieldSerializer(data={'active': 0})
        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'active': [serializers.ErrorDetail(string=message_error, code='invalid')]
        })

        serializer = StubStrictBolleanFieldSerializer(data={'active': 1})
        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'active': [serializers.ErrorDetail(string=message_error, code='invalid')]
        })

        serializer = StubStrictBolleanFieldSerializer(data={'active': 'True'})
        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'active': [serializers.ErrorDetail(string=message_error, code='invalid')]
        })

        serializer = StubStrictBolleanFieldSerializer(data={'active': 'False'})
        serializer.is_valid()
        self.assertEqual(serializer.errors, {
            'active': [serializers.ErrorDetail(string=message_error, code='invalid')]
        })

    def test_is_valid(self):
        class StubStrictBolleanFieldSerializer(serializers.Serializer):  # pylint: disable=abstract-method
            active = StrictBooleanField()

        serializer = StubStrictBolleanFieldSerializer(data={'active': True})
        serializer.is_valid()
        self.assertEqual(serializer.validated_data, {'active': True})

        serializer = StubStrictBolleanFieldSerializer(data={'active': False})
        serializer.is_valid()
        self.assertEqual(serializer.validated_data, {'active': False})
