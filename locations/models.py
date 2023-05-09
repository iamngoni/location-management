from django.db import models
from django.db.models import QuerySet

from econet.model import SoftDeleteModel


class Area(SoftDeleteModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        ordering = ("name",)
        table_prefix = "area"

    def create_shop(self, name, description):
        shop = Shop.objects.create(area=self, name=name, description=description)
        return shop

    def get_shops(self) -> QuerySet:
        return self.shops.all()


class Shop(SoftDeleteModel):
    area = models.ForeignKey(
        "locations.Area",
        on_delete=models.CASCADE,
        related_name="shops",
        blank=False,
        null=False,
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.area.name}"

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        ordering = ("name",)
        table_prefix = "shop"
