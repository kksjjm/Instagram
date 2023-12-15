from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience

class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"

class ExpListSerializer(ModelSerializer):
    class Meta:
        model = Experience
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "descriptions",
            "price",
            "category",
            "host",
        )

class ExpDetailSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"