from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):
    
    rooms = models.ManyToManyField(
        "rooms.Room",
        blank=True,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
