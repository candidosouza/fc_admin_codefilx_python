from typing import Any

from rest_framework import serializers

from __seedwork.domain.validators import DRFValidator, StrictCharField, BooleanField


class CategoryRules(serializers.Serializer):
    name = StrictCharField(max_length=255, min_length=3)
    description = StrictCharField(required=False, allow_null=True, allow_blank=True)
    is_active = BooleanField(required=False)
    created_at = serializers.DateTimeField(required=False)


class Categoryvalidator(DRFValidator):
    def validate(self, data: Any) -> bool:
        rules = CategoryRules(data=data)
        return super().validate(rules)


class CategoryValidatorFactory:
    @staticmethod
    def create():
        return Categoryvalidator()