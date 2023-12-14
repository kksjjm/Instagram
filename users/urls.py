from django.urls import path
from . import views

urlpatterns = [
    path("signin", views.UserSignIn.as_view()),
    path("me", views.MyProfile.as_view()),
    path("@<str:username>", views.PublicUserProfile.as_view()),
    path("change-password", views.ChangeUserPassword.as_view()),
]