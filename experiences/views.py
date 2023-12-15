from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

class Perks(APIView):
    def get(self, reqeust):
        all_perks = models.Perk.objects.all()
        serializer = serializers.PerkSerializer(all_perks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.PerkSerializer(data=request.data)
        if serializer.is_valid():
            new_perk = serializer.save()
            serializer = serializers.PerkSerializer(new_perk)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Perk.objects.get(pk=pk)
        except models.Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = serializers.PerkSerializer(perk)
        return Response(serializer.data)
    
    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = serializers.PerkSerializer(
            perk, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            alter_perk = serializer.save()
            serializer = serializers.PerkSerializer(alter_perk)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Experiences(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_experiences = models.Experience.objects.all()
        serializer = serializers.ExpListSerializer(
            all_experiences,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ExpDetailSerializer(data=request.data)
        if serializer.is_valid():
            new_experience = serializer.save()
            serializer = serializers.ExpDetailSerializer(new_experience)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ExperiencesDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Experience.objects.get(pk=pk)
        except models.Experience.DoesNotExist:
            raise NotFound
    
    def get(self, reqeust, pk):
        experience = self.get_object(pk)
        serializer = serializers.ExpDetailSerializer(experience)
        return Response(serializer.data)
    
    def put(self, request, pk):
        experience = self.get_object(pk)
        serializer = serializers.ExpDetailSerializer(
            experience,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_exp = serializer.save()
            serializer = serializers.ExpDetailSerializer(new_exp)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        experience = self.get_object(pk)
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
