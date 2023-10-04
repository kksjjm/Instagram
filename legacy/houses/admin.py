from django.contrib import admin
from .models import House
#document : https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

# Register your models here.
@admin.register(House) #decorator : we control House using House admin
class HouseAdmin(admin.ModelAdmin):
    #manage how to show the fields
    fields = (
        "name", 
        "price_per_night", 
        "address", 
        ("max_guest_number", "pet_allowed"),
        "owner"
    )

    # admin에 어떤 column을 추가할 것인지 
    list_display = (       
        "name",
        "price_per_night",
        "address",
        "max_guest_number",
        "pet_allowed",
        "owner")

    #filter를 추가
    list_filter = ("price_per_night", "pet_allowed")

    #search바 를 추가 
    search_fields = ("name", )

    #리스트에서 수정이 가능하도록 설정 하기 
    list_editable = ("price_per_night", "max_guest_number", "pet_allowed")

    #링크를 연결시킬 column을 지정
    # list_display_links = ("name", "address")

    #수정을 불가능하게 하고 싶은 경우 
    # exclude = ("name",)

