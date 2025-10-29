from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .serializer import InstagramSerializer
from .models import Instagram
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt 


def register(req):
    message=""
    if req.method=="POST":

        user_data={
        "username":req.POST.get("username"),
        "email":req.POST.get("email"),
        "password":req.POST.get("password"),
       "mobile":req.POST.get("mobile")
        }

        if Instagram.objects.filter(username=user_data["username"]).exists():
            message="user Already Exists"
            return render(req, "register.html", {"message": message})

        hashed_password=bcrypt.hashpw(user_data["password"].encode("utf-8"),bcrypt.gensalt(10))
        user_data["password"]=hashed_password.decode("utf-8")

        serializer=InstagramSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            message="Registeration sucessful"
            return redirect("/login")
        else:
            message=serializer.errors
    return render(req,"register.html",{"message":message})



def login(req):
    message=""
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")

        user=Instagram.objects.get(username=username)
        if not user:
            return render(req, "login.html", {"message": "User does not exist"})
        
        
        if bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8")):
            req.session["user"]=username
            message="login sucessfull"
            
        else:
            message="Invalid password"
    return render(req,"login.html",{"message":message})
    
    # return render(req,"login.html",{"message":"login"})