from django.db import models
from common.models import CommonModel, Product


class Room(Product):
    # choices
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room") 
        SHARED_ROOM = ("shared room", "Shared Room")

    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    pet_friendly = models.BooleanField(
        default = True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    # ORM
    def total_amenities(self):
        return self.amenities.count()

class Amenity(CommonModel):
    class Meta:
        verbose_name_plural = "Amenities"