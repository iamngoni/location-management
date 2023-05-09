#
#  urls.py
#  econet
#
#  Created by Ngonidzashe Mangudya on 9/5/2023.
#  Copyright (c) 2023 ModestNerds, Co


from django.urls import include, path

urlpatterns = [
    path("", include("api.views.locations.urls")),
]
