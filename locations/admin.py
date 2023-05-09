from django.contrib import admin

from .models import Area, Shop


@admin.register(Area, Shop)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
