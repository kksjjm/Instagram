from django.contrib import admin
from .models import Review
from common.admin import UserActAdmin

@admin.register(Review)
class ReviewAdmin(UserActAdmin):
    list_display = (
        "__str__",
        "descriptions",
        "created_at"
    )
    list_filter = (
        "rating",
        "created_at"
    )