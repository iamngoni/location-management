from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from locations.models import Area, Shop


class AreasTest(APITestCase):
    def test_creates_area(self):
        url = reverse("areas")
        data = {"name": "Marondera"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ShopsTest(APITestCase):
    def setUp(self) -> None:
        area = Area(name="Marondera")
        area.save()
        self.area = area

    def test_creates_shop(self):
        url = reverse("shops")
        data = {"area": self.area.id, "name": "LongChengPlaza"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_shops_saved_in_uppercase(self):
        url = reverse("shops")
        data = {"area": self.area.id, "name": "LongChengPlaza"}
        self.client.post(url, data, format="json")
        shop = Shop.objects.first()
        # check if shop's name is uppercase
        self.assertEqual(shop.name, shop.name.upper())

    def test_doesnt_allow_special_characters(self):
        url = reverse("shops")
        data = {"area": self.area.id, "name": "Long Cheng Plaza"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
