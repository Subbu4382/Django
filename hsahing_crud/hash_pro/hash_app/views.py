from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import UsersSerializer
from .models import Users
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt 
# Create your views here.


def get_users(req):
    data=Users.objects.all()
    serializer=UsersSerializer(data,many=True)
    return JsonResponse({"data":serializer.data})
    
@csrf_exempt
def reg_user(req):
    try:
        data=json.loads(req.body)
        password=data["password"].encode("utf-8")
        hashed_password=bcrypt.hashpw(password,bcrypt.gensalt(10))
        data["password"]=hashed_password.decode("utf-8")

        serializer=UsersSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse({"sucess":"user created sucessfully "})
        else:
           return JsonResponse({"error": serializer.errors})

    except Exception as e:
       return JsonResponse({"msg":str(e)})
    
@csrf_exempt
def update_user(req):
    try:
        user_data=json.loads(req.body)
        user_exists=Users.objects.get(mobile=user_data["mobile"])
        if user_data["password"]:
            password=user_data["password"].encode("utf-8")
            hashed_password=bcrypt.hashpw(password,bcrypt.gensalt(10))
            user_data["password"]=hashed_password.decode("utf-8")

        serializer=UsersSerializer(user_exists,data=user_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"user updated sucessfully"})
        else:
            return JsonResponse({"msg":"failed to update"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})
    
@csrf_exempt
def delete_user(req):
    try:
       data=json.loads(req.body)
       user_exists=Users.objects.get(mobile=data["mobile"])
       if user_exists:
          user_exists.delete()
          return JsonResponse({"sucess":"user deleted sucessfully"})
    except:
        return JsonResponse({"msg":"user not foun"})
