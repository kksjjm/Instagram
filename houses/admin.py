from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House) #decorator : we control House using House admin
class HouseAdmin(admin.ModelAdmin):
    pass
