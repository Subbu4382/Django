from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,JsonResponse
# Create your views here.



def get_users(req):
    if req.method=="GET":
        stu_data=Student.objects.all() #for fetching all the records from the table
        dict_data=stu_data.values() # for converting the query object into dictionary
        return JsonResponse({"user data":list(dict_data)})

