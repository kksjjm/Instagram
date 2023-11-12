from django.urls import path
from .views import WhishLists, WhishListsDetail, WishListToggle

urlpatterns = [
    path("",WhishLists.as_view()),
    path("<int:pk>", WhishListsDetail.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", WishListToggle.as_view()),
]
