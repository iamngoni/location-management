#
#  payload.py
#  econet
#
#  Created by Ngonidzashe Mangudya on 9/5/2023.
#  Copyright (c) 2023 ModestNerds, Co
from rest_framework import serializers

from locations.models import Area


class AreaPayloadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(
        max_length=255,
        required=False,
    )
    is_active = serializers.BooleanField(default=True)

    def validate(self, attrs):
        if not attrs["name"].isalnum():
            raise serializers.ValidationError(
                {"name": "Name must not contain special characters"}
            )

        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance


class ShopPayloadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(
        max_length=255,
        required=False,
    )
    is_active = serializers.BooleanField(default=True)
    area = serializers.CharField(max_length=255)

    def validate(self, attrs):
        area = Area.get_item_by_id(attrs["area"])
        if not area:
            raise serializers.ValidationError({"area": "Area does not exist"})

        return attrs
