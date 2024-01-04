import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from users.models import User

class KSAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None) #반환할때, 튜플로 반환 
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(f"No User {username}!!")
        
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Jwt")
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )
        pk = decoded.get('pk')
        if not pk:
            raise exceptions.AuthenticationFailed("Invalid Token!!")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found!!")