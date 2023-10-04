from django.contrib import admin
from .models import Room, Amenity
from common.admin import CommonAdmin, ProductAdmin

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "host",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "country",
        "price",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "descriptions",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )