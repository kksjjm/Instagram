from django.contrib import admin
from .models import Booking
from common.admin import UserActAdmin

@admin.register(Booking)
class BookingAdmin(UserActAdmin):
    list_display = (
        "user",
        "status",
        "room",
        "experience",
        "check_in",
        "check_out",
        "created_at",
        "updated_at"
    )
    list_filter = (
        "kind",
    )
