from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from wishlists.models import Wishlist
from users.serializers import SimpleUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer

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
    is_liked = SerializerMethodField()
    review_set = ReviewSerializer(many=True, read_only=True)
    photo_set = PhotoSerializer(many=True, read_only=True)
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
            "is_liked",
            "review_set",
            "photo_set",
        )
    def get_rating(self, room): #format 지켜야함 
        return room.rating()
    
    def get_is_host(self, room):
        request = self.context["request"]
        return room.host == request.user

    def get_is_liked(self, room):
        request = self.context["request"]
        wishlists = Wishlist.objects.filter(user=request.user)
        return wishlists.filter(rooms__pk=room.pk).exists()
        # is_liked = False
        # for wishlist in wishlists:
        #     is_liked = wishlist.rooms.filter(pk=room.pk).exists()
        #     if is_liked == True:
        #         break
        # return is_liked

class RoomDetailSerializer(ModelSerializer):
    
    host = SimpleUserSerializer(read_only=True) #request로 부터 받지 않게 하기 위해 
    amenities = AmenitySerializer(many=True, read_only=True) 
    category = CategorySerializer(read_only=True)
    rating = SerializerMethodField()
    is_host = SerializerMethodField()
    is_liked = SerializerMethodField()
    review_set = ReviewSerializer(many=True, read_only=True)
    photo_set = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
    
    def get_rating(self, room): #format 지켜야함 
        return room.rating()

    def get_is_host(self, room):
        request = self.context["request"]
        return room.host == request.user
    
    def get_is_liked(self, room):
        request = self.context["request"]
        wishlists = Wishlist.objects.filter(user=request.user)
        return wishlists.filter(rooms__pk=room.pk).exists() #manyTomany field일 때 
        # is_liked = False
        # for wishlist in wishlists:
        #     is_liked = wishlist.rooms.filter(pk=room.pk).exists()
        #     if is_liked == True:
        #         break
        # return is_liked
    