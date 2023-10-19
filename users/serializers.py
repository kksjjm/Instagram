from rest_framework.serializers import ModelSerializer
from .models import User

class HostUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
        )