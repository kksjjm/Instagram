from django.db import models
from common.models import BasicModel

class ChatRoom(BasicModel):
    # name = models.CharField(
    #     max_length=20,
    # )
    users = models.ManyToManyField(
        "users.User",
    )
    
    def __str__(self):
        return f"chat from {self.created_at} to {self.updated_at}"

class Message(BasicModel):
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    text = models.TextField()
    room = models.ForeignKey(
        "dms.ChatRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}'s message at {self.created_at}"
