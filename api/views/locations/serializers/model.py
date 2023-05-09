#
#  model.py
#  econet
#
#  Created by Ngonidzashe Mangudya on 9/5/2023.
#  Copyright (c) 2023 ModestNerds, Co

from rest_framework import serializers

from locations.models import Area


class AreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"
