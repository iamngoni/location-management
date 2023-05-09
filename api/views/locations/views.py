#
#  views.py
#  econet
#
#  Created by Ngonidzashe Mangudya on 9/5/2023.
#  Copyright (c) 2023 ModestNerds, Co

from rest_framework.views import APIView

from api.views.locations.serializers.model import (
    AreaModelSerializer,
    ShopModelSerializer,
)
from api.views.locations.serializers.payload import (
    AreaPayloadSerializer,
    ShopPayloadSerializer,
)
from locations.models import Area, Shop
from services.helpers.api_pagination import ApiPagination
from services.responses.api_response import ApiResponse
from loguru import logger


class AreasView(APIView, ApiPagination):
    authentication_classes = ()
    serializer_class = AreaPayloadSerializer

    def get(self, request):
        try:
            if request.query_params.get("limit") is not None:
                self.page_size = request.query_params.get("limit")

            areas = Area.objects.all()
            areas = self.paginate_queryset(areas, request, view=self)
            areas = AreaModelSerializer(areas, many=True).data
            return ApiResponse(
                data={
                    "areas": self.get_paginated_response(areas).data,
                }
            )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)

    def post(self, request):
        try:
            payload = self.serializer_class(data=request.data)
            if payload.is_valid():
                area = Area.objects.create(**payload.validated_data)
                return ApiResponse(
                    num_status=201,
                    data={
                        "area": AreaModelSerializer(area).data,
                    },
                )
            else:
                logger.error(payload.errors)
                return ApiResponse(
                    num_status=400, bool_status=False, issues=payload.errors
                )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)


class AreaDetailsView(APIView):
    authentication_classes = ()
    serializer_class = AreaPayloadSerializer

    def get(self, request, area_id):
        try:
            area = Area.get_item_by_id(area_id)
            if area is None:
                logger.error("Area not found")
                return ApiResponse(
                    num_status=404, bool_status=False, message="Area not found"
                )

            return ApiResponse(
                data={
                    "area": AreaModelSerializer(area).data,
                }
            )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)

    def put(self, request, area_id):
        try:
            area = Area.get_item_by_id(area_id)
            if area is None:
                logger.error("Area not found")
                return ApiResponse(
                    num_status=404, bool_status=False, message="Area not found"
                )

            payload = self.serializer_class(data=request.data)
            if payload.is_valid():
                area = payload.update(
                    instance=area, validated_data=payload.validated_data
                )
                return ApiResponse(
                    data={
                        "area": AreaModelSerializer(area).data,
                    }
                )
            else:
                logger.error(payload.errors)
                return ApiResponse(
                    num_status=400, bool_status=False, issues=payload.errors
                )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)


class AreaShopsView(APIView, ApiPagination):
    authentication_classes = ()

    def get(self, request, area_id):
        try:
            if request.query_params.get("limit") is not None:
                self.page_size = request.query_params.get("limit")

            area = Area.get_item_by_id(area_id)
            if area is None:
                logger.error("Area not found")
                return ApiResponse(
                    num_status=404, bool_status=False, message="Area not found"
                )

            shops = area.shops.all()
            shops = self.paginate_queryset(shops, request, view=self)
            shops = ShopModelSerializer(shops, many=True).data
            return ApiResponse(
                data={
                    "shops": self.get_paginated_response(shops).data,
                }
            )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)


class ShopsView(APIView, ApiPagination):
    authentication_classes = ()
    serializer_class = ShopPayloadSerializer

    def get(self, request):
        try:
            if request.query_params.get("limit") is not None:
                self.page_size = request.query_params.get("limit")

            shops = Shop.objects.all()
            shops = self.paginate_queryset(shops, request, view=self)
            shops = ShopModelSerializer(shops, many=True).data
            return ApiResponse(
                data={
                    "shops": self.get_paginated_response(shops).data,
                }
            )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)

    def post(self, request):
        try:
            payload = self.serializer_class(data=request.data)
            if payload.is_valid():
                area = Area.get_item_by_id(payload.validated_data.get("area"))
                if area is None:
                    logger.error("Area not found")
                    return ApiResponse(
                        num_status=404,
                        bool_status=False,
                        message="Area not found",
                    )

                shop = area.create_shop(**payload.validated_data)
                return ApiResponse(
                    num_status=201,
                    data={
                        "shop": ShopModelSerializer(shop).data,
                    },
                )
            else:
                logger.error(payload.errors)
                return ApiResponse(
                    num_status=400, bool_status=False, issues=payload.errors
                )
        except Exception as exc:
            logger.error(exc)
            return ApiResponse(num_status=500, bool_status=False)
