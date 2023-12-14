from rest_framework.serializers import ModelSerializer
from .models import User

class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
        )
class MyProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        )

class PublicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
            "email",
        )