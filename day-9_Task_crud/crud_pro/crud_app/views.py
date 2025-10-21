from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def update_user(req,id):
    data=json.loads(req.body)
    emp=Employee.objects.get(emp_id=id)
    if "emp_id" in data:
        emp.emp_id=data.emp_id
    if "emp_name" in data:
        emp.emp_name=data.emp_name
    if "emp_ph" in data:
        emp.emp_ph=data.emp_ph
    if "emp_salary" in data:
        emp.emp_salary=data.emp_salary

    emp.save()
    return JsonResponse({"sucess":"updated sucessfully"})


def get_users(req):
    user_data=Employee.objects.all().values()
    return HttpResponse(list(user_data))


@csrf_exempt
def reg_user(req):
    data=json.loads(req.body)
    emp=Employee.objects.create(
        emp_id=data["emp_id"],
        emp_name=data["emp_name"],
        emp_ph=data["emp_ph"],
        emp_salary=data["emp_salary"]
    )
    return JsonResponse({"sucess":"user created sucessfully"})


@csrf_exempt
def delete_user(req,id):
    emp=Employee.objects.get(emp_id=id)
    emp.delete()
    return HttpResponse("user  "+emp.emp_name +"  deleted")