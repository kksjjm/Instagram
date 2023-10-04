from django.db import models
from common.models import UserAct

class Review(UserAct):

    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.user} \ {self.rating}"