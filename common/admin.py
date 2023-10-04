from django.contrib import admin

# Register your models here.
class CommonAdmin(admin.ModelAdmin):
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

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "host",
        "address",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "country",
        "price",
        "created_at",
        "updated_at",
    )

class UserActAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "room",
        "experience",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at"
    )