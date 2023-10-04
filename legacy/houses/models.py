from django.db import models
# document : https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.DateTimeField

# Create your models here.
class House(models.Model):
    
    """Model definition of Houses"""

    name = models.CharField(
        max_length=140,
    )
    # images = models.ImageField()
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=140,
    )
    max_guest_number = models.PositiveSmallIntegerField(
        default=1,
        help_text = "최대 인원수 이상으로는 숙박이 불가능 합니다."
    )
    pet_allowed = models.BooleanField(
        verbose_name = "Is pets Allowed?",
        default=True,
    )

    # relationship
    owner = models.ForeignKey(
        "users.User", 
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.name

# User를 커스터마이징 하는 방법 1) 기본 User에 추가적인 속성을 추가하는 방법 2) 새로 User를 셋팅해서 전체를  교체하는 방법 
# 1) https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#extending-the-existing-user-model
# 2) https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
