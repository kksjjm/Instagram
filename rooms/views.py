from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import transaction
from django.utils import timezone 

from .models import Amenity, Room
from bookings.models import Booking
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from bookings.serializers import PublicBookingSerializer, CreateRoomBookingSerializer
from django.conf import settings

class Amenities(APIView):
    def get(self, request):
        all_amenity = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenity, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            ) # error의 내용 반환 

class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            return Response(NotFound)

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            alter_amenity = serializer.save()
            return Response(AmenitySerializer(alter_amenity).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
    
    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Rooms(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms, 
            many=True,
            context={"request":request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RoomDetailSerializer(data=request.data) #여기서 RoomDetail을 사용하는 이유 = 만들때는 모든 data를 포함하게 하고 싶으니까
        if serializer.is_valid():
            category_pk = request.data.get("category") #카테고리 pk받기 
            if not category_pk:
                raise ParseError("Category is required") # 잘못된 정보를 받았을 때
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                    raise ParseError("The category kind should be 'rooms'") # Room이니까, Category가 Experience인 경우에는 
            except Category.DoesNotExist:
                raise ParseError(f"Category with id #{category_pk} is not found")
            try:
                with transaction.atomic():
                    new_room = serializer.save( 
                        host=request.user, #ForeignKey
                        category=category,
                    ) #host에 로그인한 user를 할당해줌
                    amenities = request.data.get("amenities") #ManyToMany relationship
                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        new_room.amenities.add(amenity)
                    return Response(RoomListSerializer(new_room).data)
            except Exception:
                raise ParseError("Amenity is not found")
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            ) # error의 내용 반환 

class RoomDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(
            room,
            context={"request":request},
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = self.get_object(pk)
        # if not request.user.is_authenticated:
        #     raise NotAuthenticated
        if room.host != request.user:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            alter_room = serializer.save()
            return Response(RoomDetailSerializer(alter_room).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
    
    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.host != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#with pagenation
class RoomReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        # print("query_params : ", request.query_params)
        try:
            page = request.query_params.get("page",1) #page paramater가 있는지 확인하고, 없으면 1반환
            page = int(page)
        except ValueError:
            page = 1
        page_size = 3
        start = (page-1)*page_size
        end = page*page_size
        room = self.get_object(pk)
        serializer = ReviewSerializer(
            room.review_set.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                room=self.get_object(pk),
            )

            serializer = ReviewSerializer(review)
            return Response(serializer.data)

class RoomAmenities(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page-1)*page_size
        end = page*page_size
        serializer = AmenitySerializer(
            room.amenity_set.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

class RoomPhotos(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)
        if request.user != room.host:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(
                room = room,
            )
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )
        
class RoomBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        today = timezone.localtime(timezone.now()).date()
        room = self.get_room(pk)
        booking = Booking.objects.filter(
            room=room,
            kind=Booking.KindChoices.ROOM,
            check_out__gt=today #check_in greater than today
            )
        # booking = Booking.objects.filter(room__pk=pk) #이렇게도 할 수 있음
        serializer = PublicBookingSerializer(
            booking,
            many=True,
            )
        return Response(serializer.data)
    
    def post(self, request, pk):
        room = self.get_room(pk)
        serializer = CreateRoomBookingSerializer(
            data=request.data,
            )
        if serializer.is_valid():
            new_booking = serializer.save(
                room=room,
                user=request.user,
                status=Booking.BookingStatusChoices.RESERVED,
                kind=Booking.KindChoices.ROOM,
            )
            serializer = PublicBookingSerializer(new_booking)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )