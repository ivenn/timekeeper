from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    name = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    started = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()  # in minutes

    def __str__(self):
        return self.name


class Settings(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    session_length = models.PositiveSmallIntegerField(default=20,
                                                      validators=[MaxValueValidator(60),
                                                                  MinValueValidator(5)])  # in minutes
    break_length = models.PositiveSmallIntegerField(default=5,
                                                    validators=[MaxValueValidator(30),
                                                                MinValueValidator(1)])  # in minutes

    def __str__(self):
        return "%s/%s " % (self.session_length, self.break_length)
