from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound 
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomSerializer

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
            return Response(serializer.errors) # error의 내용 반환 

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
            data=request.data
        )
        if serializer.is_valid():
            alter_amenity = serializer.save()
            return Response(AmenitySerializer(alter_amenity).data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Rooms(APIView):
    
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomSerializer(all_rooms)
        return Response(serializer.data)
    
    def post(self, request):
        pass

class RoomDetail(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass
    
    def put(self, request, pk):
        pass
    
    def delete(self, request, pk):
        pass