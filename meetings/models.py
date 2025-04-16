from django.db import models
from django.contrib.auth import get_user_model
from datetime import time

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey('Room', on_delete=models.CASCADE) #if the room is deleted,
                                                               #all meetings in that room are also deleted
    participants = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f"{self.title} at {self.start_time.strftime('%H:%M')} on {self.date.strftime('%Y-%m-%d')}"

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} on floor {self.floor_number}, room {self.room_number}"

    