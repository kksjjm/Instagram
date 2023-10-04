from django.db import models
from common.models import CommonModel, Product

# Create your models here.
class Experience(Product):

    perks = models.ManyToManyField(
        "experiences.Perk"
    )
    
class Perk(CommonModel):

    """ What is included in an Experience """

    details = models.CharField(
        max_length=250,
    )