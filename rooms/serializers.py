from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from users.serializers import HostUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "descriptions",
        ) # show all column

class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_host = SerializerMethodField()
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
            "review_set",
        )
    def get_rating(self, room): #format 지켜야함 
        return room.rating()
    def get_is_host(self, room):
        request = self.context["request"]
        return room.host == request.user

class RoomDetailSerializer(ModelSerializer):
    
    host = HostUserSerializer(read_only=True) #request로 부터 받지 않게 하기 위해 
    amenities = AmenitySerializer(many=True, read_only=True) 
    category = CategorySerializer(read_only=True)
    rating = SerializerMethodField()
    is_host = SerializerMethodField()
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
    
    def get_rating(self, room): #format 지켜야함 
        return room.rating()

    def get_is_host(self, room):
        request = self.context["request"]
        return room.host == request.user
    
    