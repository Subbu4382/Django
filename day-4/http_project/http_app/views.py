from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#get -> To get data
#put
#post
#patch
#delete

# @csrf_exempt
# def welcome(request):
#     # for prop in dir(request):
#     #     print(prop)
#     print(request.method)
#     return HttpResponse("welcom to django app !")

@csrf_exempt
def welcome(request):
    if request.method=="GET":
        return HttpResponse("welcome to Get request !")
    else:
        return HttpResponse("Invalid method !")



details=[{
    "id_":1,
    "name":"subbu",
    "profession":"python developer",
    "salary":200000
}
,
  {  "id_":2,
    "name":"vaishu",
    "profession":"python developer",
    "salary":20000
  }
]
def details_view(req):
    return JsonResponse ({"response":details})


def single_user(req,id):
    # return JsonResponse ({"user":id})
    for user in details:
        if id==user['id_']:
            return JsonResponse({"user_data":user})
    return JsonResponse({"msg":"user does not exist !"})

@csrf_exempt
def register_user(req):
    user_data=json.loads(req.body)
    details.append(user_data)
    print(details)
    return HttpResponse("registration is sucessfull")