from django.db import models
from common.models import BasicModel

class Photo(BasicModel):

    file = models.ImageField()
    descriptions = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return "Photo File"

class Video(BasicModel):

    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"