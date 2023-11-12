from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import MyProfileSerializer

class MyProfile(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        me = request.user
        serializer = MyProfileSerializer(me)
        return Response(serializer.data)
    
    def put(self, request):
        me = request.user
        serializer = MyProfileSerializer(
            me,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_me = serializer.save()
            serializer = MyProfileSerializer(new_me)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)