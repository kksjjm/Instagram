from django.contrib import admin
from .models import Experience, Perk
from common.admin import CommonAdmin, ProductAdmin

@admin.register(Experience)
class ExperienceAdmin(ProductAdmin):
    list_display = (
        "name",
        "descriptions",
        "start_time",
        "end_time"
    )

@admin.register(Perk)
class PerkAdmin(CommonAdmin):
    pass