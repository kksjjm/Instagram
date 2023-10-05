from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__" # 전부 보여주기 
        # exclude = ("updated_at", ) # "pk, udpated_at 빼고 보여주기"

# # -------------- legacy --------------
# # 어떻게 json으로 변환되는지 설정 
# class CategorySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(
#         required=True,
#         max_length=50,
#     )
#     kind = serializers.ChoiceField(
#         choices=Category.CategoryKindChoices.choices,
#     )
#     created_at = serializers.DateTimeField(read_only=True)

#     # called when serializer have only request.data
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)

#     # called when serializer have model.oboject and request.data
#     def update(self, instance, validated_data):
#         # dict.get(A,B) => A를 찾아보고, 없으면 B를 반환해줘 
#         instance.name = validated_data.get("name", instance.name) #validated_data에서 "name"을 찾아보고 없으면 instance.name을 반환해줘 
#         instance.kind = validated_data.get("kind", instance.kind)
#         instance.save()
#         return instance