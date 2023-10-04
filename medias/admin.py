from django.contrib import admin
from .models import Photo, Video

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = (
        "file",
        "descriptions",
        "room",
        "experience",
    )

    list_display = (
        "room",
        "experience",
        "descriptions",
    )
    pass
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
