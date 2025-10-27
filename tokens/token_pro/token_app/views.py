from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import UsersSerializer
from .models import Users
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt 
import jwt
# Create your views here.



    
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
       token=data["token"]
       decoded = jwt.decode(token, SECRET_KEY, algorithms="HS256")
       if decoded["is_login"] and decoded["admin"]:
          user_exists=Users.objects.get(mobile=data["mobile"])
          if user_exists.admin:
              return JsonResponse({"msg":"you cant delete admin"})
          user_exists.delete()
          return JsonResponse({"sucess":"user deleted sucessfully"})
       else:
           return JsonResponse({"msg":"you are not authorized to delete user"})
    except:
        return JsonResponse({"msg":"user not found"})
    


SECRET_KEY = 'django-insecure-1e5k@c7my3-hr=su7+m2y@0i8!u%0ej!unt1^q87wtyut-tpfm'

def login_user(req):
    user_data=json.loads(req.body)
    user_exists=Users.objects.get(mobile=user_data["mobile"])
    if user_exists:
        hashed_password=user_exists.password.encode("utf-8")
        password=user_data["password"].encode("utf-8")
        if bcrypt.checkpw(password,hashed_password):
            payload={
                "name":user_exists.name,
                "password":user_exists.password,
                "is_login":True,
                "admin":user_exists.admin
            }
            token=jwt.encode(payload,SECRET_KEY,algorithm="HS256")
            return JsonResponse({"msg":"login sucessfull","data":token})
        

def get_users(req):
    try:
      user_data=json.loads(req.body)
      token=user_data["token"]
      decoded=jwt.decode(token,SECRET_KEY,algorithms="HS256")
      if decoded["is_login"]:
        all_data=Users.objects.all()
        serializer=UsersSerializer(all_data,many=True)
        return JsonResponse({"data":serializer.data})
    except:
        return JsonResponse({"error":"please login to access data"})
    
