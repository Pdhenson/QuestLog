from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.db import models

# Create your models here.
class Quest(models.Model):

    user_name = models.CharField(max_length=30)
    title_field = models.CharField(max_length=30)
    date_field = models.DateField(auto_now=True)
    task_field = models.CharField(max_length=256)
    reward_field = models.CharField(max_length=100)

    def __str__(self):
        return self.title_field

class Steps(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    title_field = models.CharField(max_length=30)
    date_start = models.DateField(auto_now=True)
    step_one = models.CharField(max_length=255, default = "")
    step_two = models.CharField(max_length=255, default = "NA")
    step_three = models.CharField(max_length=255, default = "NA")
    step_four = models.CharField(max_length=255, default = "NA")
    step_five = models.CharField(max_length=255, default = "NA")
    step_one_complete = models.IntegerField(default = "0")
    step_two_complete = models.IntegerField(default = "0")
    step_three_complete = models.IntegerField(default = "0")
    step_four_complete = models.IntegerField(default = "0")
    step_five_complete = models.IntegerField(default = "0")
    completion_percent = models.FloatField(default = '0.0')

    def __str__(self):
        return self.title_field

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
