from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    started = models.DateTimeField()
    finished = models.DateTimeField()

    def __str__(self):
        return self.name


class Settings(models.Model):

    owner = models.OneToOneField(User)
    session_length_min = models.PositiveSmallIntegerField(default=20)
    break_length_min = models.PositiveSmallIntegerField(default=5)

