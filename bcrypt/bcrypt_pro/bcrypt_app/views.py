from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import StudentSerializer
from .models import Students
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt
# Create your views here.

def get_students(req):
    data=Students.objects.all()
    serializer=StudentSerializer(data,many=True)
    return JsonResponse({"data":serializer.data})

@csrf_exempt
def reg_student(req):
    try:
      data=json.loads(req.body)
      password=data["stu_password"].encode("utf-8")
      hashed_pass=bcrypt.hashpw(password,bcrypt.gensalt(10))
      data["stu_password"]=hashed_pass.decode("utf-8")
      serializer=StudentSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse({"sucess":"data saved sucessfully"})
    except Exception as e:
       return JsonResponse({"msg":e})
    
def login(req):
   try:
     stu_data=json.loads(req.body)
     Student=Students.objects.get(stu_id=stu_data["stu_id"])
     if bcrypt.checkpw(stu_data["stu_password"].encode("utf-8"),Student.stu_password.encode("utf-8")):
      return HttpResponse(f"Login Sucessfull! Welcome {Student.stu_name}")
   except Exception as e:
      return HttpResponse(e) 
   
