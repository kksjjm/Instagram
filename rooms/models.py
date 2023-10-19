from django.db import models
from common.models import CommonModel, Product


class Room(Product):
    # choices
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room") 
        SHARED_ROOM = ("shared room", "Shared Room")

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
    
    def rating(room):
        count = room.review_set.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in room.review_set.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating/count, 2)

class Amenity(CommonModel):
    class Meta:
        verbose_name_plural = "Amenities"