from django.db import models
from common.models import UserAct

class Booking(UserAct):

    class BookingStatusChoices(models.TextChoices):
        RESERVED = ("reserved", "Reserved")
        PAID = ("paid", "Paid")
        CANCELED = ("canceled", "Canceled")
        COMPLETED = ("completed", "Completed")

    # alter
    descriptions = models.TextField(
        editable=False,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # add
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveSmallIntegerField()
    # kids = models.PositiveSmallIntegerField()
    status = models.CharField(
        max_length=15,
        choices=BookingStatusChoices.choices,
    )


