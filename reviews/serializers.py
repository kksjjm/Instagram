from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import SimpleUserSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    
    user = SimpleUserSerializer(read_only=True) # User정보가 필수가 아님 --> 왜냐면 이미 있는 정보를 사용할거라서 
    class Meta:
        model = Review
        fields = (
            "user",
            "descriptions",
            "rating",
        )