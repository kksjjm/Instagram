from django.db import models

# Create your models here.
class House(models.Model):
    
    """Model definition of Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    max_guest_number = models.PositiveSmallIntegerField(default=1)
    pet_allowed = models.BooleanField(default=True)

