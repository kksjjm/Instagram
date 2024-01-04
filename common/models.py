from django.db import models

class BasicModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True) # 처음 저장될 때 
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 될때 마다 


class CommonModel(BasicModel):

    # 만약 데이터베이스에 업데이트 하고 싶지 않을 때 
    class Meta:
        abstract = True
    
    name = models.CharField(
        max_length=100,
        # default="",
    )
    descriptions = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

class Product(CommonModel):
    
    class Meta:
        abstract = True

    country = models.CharField(
        max_length=50,
        default = "Korea",
    )
    city = models.CharField(
        max_length=80,
        default = "Seoul",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
        blank=True,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    # reviews = models.ManyToManyField(
    #     "reviews.Review",
    #     blank=True,
    # )
    start_time = models.TimeField()
    end_time = models.TimeField()

class UserAct(CommonModel):

    class Meta:
        abstract = True

    class KindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    name = models.CharField(
        max_length=150,
        editable=False,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        #related_name="reviews", 이걸통해서 reverse accessor의 이름을 커스터마이징 할 수 있음
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    kind = models.CharField(
        max_length=15,
        choices=KindChoices.choices,
        null=True,
        blank=True,
        default="",
    )
