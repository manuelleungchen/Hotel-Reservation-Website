from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal

# Create your models here.

class Room(models.Model):
    unit1 = "01"
    unit2 = "02"
    unit3 = "03"
    unit4 = "04"
    unit5 = "05"
    unit6 = "06"
    unit7 = "07"
    unit8 = "08"
    unit9 = "09"
    unit10 = "10"
    unit11 = "11"
    unit12 = "12"


    level1 = "1"
    level2 = "2"
    level3 = "3"
    level4 = "4"
    level5 = "5"
    level6 = "6"
    level7 = "7"
    level8 = "8"
    level9 = "9"

    bed1 = 1
    bed2 = 2
    bed3 = 3
    bed4 = 4

    

    UNITNUMBER = [
        (unit1, "Unit 1"),
        (unit2, "Unit 2"),
        (unit3, "Unit 3"),
        (unit4, "Unit 4"),
        (unit5, "Unit 5"),
        (unit6, "Unit 6"),
        (unit7, "Unit 7"),
        (unit8, "Unit 8"),
        (unit9, "Unit 9"),
        (unit10, "Unit 10"),
        (unit11, "Unit 11"),
        (unit12, "Unit 12"),
    ]

    FLOORNUMBER = [
        (level1, "Ground Level"),
        (level2, "2nd Level"),
        (level3, "3rd Level"),
        (level4, "4th Level"),
        (level5, "5th Level"),
        (level6, "6th Level"),
        (level7, "7th Level"),
        (level8, "8th Level"),
        (level9, "9th Level")
    ]

    BEDSNUMBER = [
        (bed1, "1 Bedroom"),
        (bed2, "2 Bedrooms"),
        (bed3, "3 Bedrooms"),
        (bed4, "4 Bedrooms"),
    ]

    floorNumber = models.CharField(max_length=2, choices=FLOORNUMBER)
    roomNumber = models.CharField(max_length=2, choices=UNITNUMBER)
    bedsNumber = models.PositiveSmallIntegerField(choices=BEDSNUMBER)
    unitNumber = models.CharField(max_length=4, editable=False)
    available = models.BooleanField(default=True)

    def save(self):
        self.unitNumber = self.floorNumber + self.roomNumber
        super(Room, self).save()

    def __str__(self):
        return self.unitNumber

    class Meta:
        ordering = ["-unitNumber"]


class Reservation(models.Model):

    def tomorrow():
        return timezone.now() + timezone.timedelta(days=1)

    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    endDate = models.DateField(default=tomorrow().strftime("%Y-%m-%d"))  # a date

    def __str__(self):
        return self.guest.username + " - " + self.room.unitNumber

    class Meta:
        ordering = ["-room"]
















