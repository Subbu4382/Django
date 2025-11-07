from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Coders
# Create your views here.


def users(request):
    users=Coders.objects.all().values()
    return JsonResponse({"data":list(users)})

@ csrf_exempt
def reg_user(req):
    user_name=req.POST.get("name")
    user_age=req.POST.get("age")
    print(user_name,user_age)
    coder= Coders.objects.create(name=user_name,age=user_age)
    coder.save()

    return HttpResponse("user details saved sucessfully")

