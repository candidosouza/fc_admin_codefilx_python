from typing import Dict
from rest_framework import serializers
from core.__seedwork.domain.validators import DRFValidator, StrictBooleanField, StrictCharField




class CategoryRules(serializers.Serializer): # pylint: disable=abstract-method
    name = StrictCharField(max_length=255, min_length=3)
    description = StrictCharField(
        required=False, allow_null=True, allow_blank=True)
    is_active = StrictBooleanField(required=False)
    created_at = serializers.DateTimeField(required=False)


class CategoryValidator(DRFValidator): # pylint: disable=too-few-public-methods
    def validate(self, data: Dict) -> bool:
        rules = CategoryRules(data=data if data is not None else {})
        return super().validate(rules)


class CategoryValidatorFactory:  # pylint: disable=too-few-public-methods
    @staticmethod
    def create():
        return CategoryValidator()
