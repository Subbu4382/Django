from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=30)
    emp_ph=models.CharField(max_length=10,unique=True)
    emp_salary=models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'crud_app_employee'