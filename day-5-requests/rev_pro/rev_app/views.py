from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def rev(request):
    # to get json data
    userdata=json.loads(request.body)
    print(userdata)
    print(request.POST)

    # to get form data
    print(request.POST.get("username"))   
    print(request.POST.get("branch"))

    return HttpResponse("day-5 django")