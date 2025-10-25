from django.db import models

# Create your models here.
class Students(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    stu_branch=models.CharField(max_length=20)
    stu_password=models.CharField(max_length=255)
    stu_ph=models.CharField(max_length=10,unique=True)