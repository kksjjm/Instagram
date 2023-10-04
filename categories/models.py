from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    """ Categories of Room OR Experience """

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    kind = models.CharField(
        max_length=20,
        choices=CategoryKindChoices.choices,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.kind}: {self.name}"