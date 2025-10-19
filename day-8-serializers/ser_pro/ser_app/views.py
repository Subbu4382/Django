from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializer import StudentSerializer
# Create your views here.

# @csrf_exempt
# def update_user(req,id):
  
#     try:
#       user_data=json.loads(req.body)
#     except:
#         return JsonResponse({"error":"Invalid json"})
    

#     try:
#         student=Student.objects.get(stu_id=id)
#     except:
#         return JsonResponse({"error":"user not found"})
#     if 'stu_id' in user_data:
#            student.stu_id=user_data["stu_id"]
#     if 'stu_name' in user_data:
#            student.stu_name=user_data["stu_name"]
#     if 'stu_branch' in user_data:
#            student.stu_branch=user_data["stu_branch"]
#     if 'stu_ph' in user_data:
#            student.stu_ph=user_data["stu_ph"]
#     student.save()

#     return JsonResponse({'sucess':"user updated sucessfully"})
        

@csrf_exempt
def delete_user(req,id):
    try:
         existing_stu=Student.objects.get(stu_id=id)
         existing_stu.delete()
         return JsonResponse({"sucess":"user deleted"})
    except:
         return HttpResponse("user not found")
    


def get_users(req):
     all_data=Student.objects.all()
     serialized_data=StudentSerializer(all_data,many=True)
     print(serialized_data.data)
     return JsonResponse({"data":serialized_data.data})


def update_user(req,id):
     user_data=json.loads(req.body)
     exists=Student.objects.get(stu_id=id)

     StudentSerializer(data=user_data,partial=True)
     if serialized_data.is_valid():
          serialized_data.save()