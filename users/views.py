import jwt
from django.conf import settings 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import MyProfileSerializer, PublicUserSerializer
from users.models import User

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
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        
class UserSignIn(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = MyProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password) # 이렇게 작업해야함 
            user.save()
            serializer = MyProfileSerializer(user)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class PublicUserProfile(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serilaizer = PublicUserSerializer(user)
        return Response(serilaizer.data)
    # 코드첼린지 => User에 딸린 집, Exp, 리뷰를 볼수 있게 해보기 

class ChangeUserPassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogIn(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request=request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return Response({"Log-In": "Wellcome!!"})
        else:
            return Response({"error": "Wrong Username or Password!!"})

class UserLogOut(APIView):
    def post(self, request):
        logout(request)
        return Response({"Log-Out":"See you!!"})

class JWTLogin(APIView):
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request=request,
            username=username,
            password=password,
        )
        
        if user:
            token = jwt.encode(
                {"pk":user.pk}, 
                settings.SECRET_KEY,
                algorithm="HS256",
                )
            return Response({"token": token})
        else:
            return Response ({"error": "wrong username or password"})
