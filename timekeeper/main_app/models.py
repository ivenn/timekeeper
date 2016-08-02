from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    started = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(default=1)  # in minutes

    def __str__(self):
        return self.name


class Settings(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    session_length = models.PositiveSmallIntegerField(default=20)  # in minutes
    break_length = models.PositiveSmallIntegerField(default=5)  # in minutes

    def __str__(self):
        return "%s/%s " % (session_length, break_length)