from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from locations.models import Area, Shop


class ShopsTest(APITestCase):
    def setUp(self) -> None:
        area = Area(name="BelvedereSouth")
        area.save()
        self.area = area

    def test_shops_saved_in_uppercase(self):
        """
        @description: Test shops saved in uppercase
        @return:
        """
        url = reverse("shops")
        data = {"area": self.area.id, "name": "Long Cheng Plaza"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        shop = Shop.objects.first()
        # check if shop's name is uppercase
        self.assertEqual(shop.name, shop.name.upper())
