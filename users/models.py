from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # Choices
    class GenderChoices(models.TextChoices):
        # (value for DB, Text showed in Admin)
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
    class CurrencyChoices(models.TextChoices):
        WON = ("won", "원화")
        USD = ("usd", "US Dollar")

    # 비활성화
    first_name = models.CharField(
        max_length=150, 
        editable=False,
    )
    last_name = models.CharField(
        max_length=150, 
        editable=False,
    )

    # 새로운 field
    name = models.CharField(
        max_length=150, 
        default="",
    ) #다른 column에 있는 정보를 가져오려면 어떻게 해야할끼?
    is_host = models.BooleanField(
        default=False,
    )
    avatar = models.URLField(
        blank=True,
    )
    gender = models.CharField(
        max_length=10, 
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )