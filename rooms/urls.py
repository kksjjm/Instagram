from django.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
]