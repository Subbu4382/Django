from django.db import models


# Create your models here.
class Celebrities(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=30)
    followers = models.CharField(max_length=10)
    nationality = models.CharField(max_length=20, default="Indian")
    DOB = models.DateField()
    profile_pic = models.URLField(default="Empty")
