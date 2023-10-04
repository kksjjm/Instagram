from django.contrib import admin
from common.admin import CommonAdmin
from .models import Category

@admin.register(Category)
class CategoryAdmin(CommonAdmin):
    list_display = (
        "name",
        "kind",
    )

    list_filter = (
        "kind",
    )

