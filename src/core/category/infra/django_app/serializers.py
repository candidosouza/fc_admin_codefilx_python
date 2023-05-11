from rest_framework import serializers


class CategorySerializer(serializers.Serializer): # pylint: disable=abstract-method
    name = serializers.CharField()
    description = serializers.CharField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False)
