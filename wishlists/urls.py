from django.urls import path
from .views import WhishLists, WhishListsDetail

urlpatterns = [
    path("",WhishLists.as_view()),
    path("<int:pk>", WhishListsDetail.as_view()),
]
