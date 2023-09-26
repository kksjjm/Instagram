from django.db import models

# Create your models here.
class House(models.Model):
    
    """Model definition of Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)

