from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.status import HTTP_200_OK
from .models import Wishlist
from .serializers import WishlistSerializer

class WhishLists(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(
            all_wishlists, 
            many=True,
            context={"request":request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)


class WhishListsDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializer = WishlistSerializer(
            wishlist,
            context={"request":request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        wishlist = self.get_object(pk, request.user)       
        serializer = WishlistSerializer(
            wishlist,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            alter_wishlist = serializer.save()
            serializer = WishlistSerializer(alter_wishlist,
                                            context={"request":request},)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status=HTTP_200_OK)
