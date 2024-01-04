
from .models import Category
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .serializers import CategorySerializer

class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save() # call "create" method in CategorySerializer
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist: 
            raise NotFound # stop reading code below

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True, # just want update
        )
        if serializer.is_valid():
            updated_category = serializer.save() # call "update" method 
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)

# -------------- legacy --------------
#from rest_framework.viewsets import ModelViewSet

#class CategoryViewSet(ModelViewSet):
    
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# from .serializers import CategorySerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from rest_framework.status import HTTP_204_NO_CONTENT

# @api_view(["GET","POST"])
# def categories(request):
#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         print(request.data)
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializer.save() # call "create" method in CategorySerializer
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializer.errors)

# @api_view(["GET", "PUT", "DELETE"])
# def category(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist: 
#         raise NotFound # stop reading code below

#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = CategorySerializer(
#             category,
#             data=request.data,
#             partial=True, # just want update
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save() # call "update" method 
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)
    
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)