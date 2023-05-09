#
#  urls.py
#  econet
#
#  Created by Ngonidzashe Mangudya on 9/5/2023.
#  Copyright (c) 2023 ModestNerds, Co
from django.urls import path

from api.views.locations.views import (
    AreasView,
    AreaDetailsView,
    AreaShopsView,
    ShopsView,
    ShopDetailsView,
)

urlpatterns = [
    path("areas", AreasView.as_view(), name="areas"),
    path("areas/<str:area_id>", AreaDetailsView.as_view(), name="area_details"),
    path("areas/<str:area_id>/shops", AreaShopsView.as_view(), name="area_shops"),
    path("shops", ShopsView.as_view(), name="shops"),
    path("shops/<str:shop_id>", ShopDetailsView.as_view(), name="shop_details"),
]
