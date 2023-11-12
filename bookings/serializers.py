from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils import timezone
from .models import Booking

class CreateRoomBookingSerializer(ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )
    #customized validation : validate_name of field
    def validate_check_in(self, value):
        today = timezone.localtime(timezone.now()).date()
        if today > value:
            raise serializers.ValidationError("The check_in date must be in the future!")
        else:
            return value

    def validate_check_out(self, value):
        today = timezone.localtime(timezone.now()).date()
        if today > value:
            raise serializers.ValidationError("The check_out date must be in the future!")
        else:
            return value
        
    def validate(self, data):
        if data["check_in"] > data["check_out"]:
            raise serializers.ValidationError("Check_in date must be earlier than check_out date")
        
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError("There are already reservations")
        
        return data
        
class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
        )