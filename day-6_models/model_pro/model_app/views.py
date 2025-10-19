from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Coders
# Create your views here.


def details(request):
    return HttpResponse ("day-6 of django learning")

@ csrf_exempt
def reg_user(req):
    user_name=req.POST.get("username")
    user_age=req.POST.get("userage")
    print(user_name,user_age)
    coder= Coders.objects.create(name=user_name,age=user_age)
    coder.save()

    return HttpResponse("user details saved sucessfully")

