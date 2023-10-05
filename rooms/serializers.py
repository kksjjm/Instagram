from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__" # show all column

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__" # show all column