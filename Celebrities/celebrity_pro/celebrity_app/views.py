from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Celebrities
from .serializer import CelebritySerializer
import cloudinary

# Create your views here.
@csrf_exempt
def register(req):
    message=""
    if req.method=="POST":
        register_data={
        "name":req.POST.get("name"),
        "age":req.POST.get("age"),
        "gender":req.POST.get("gender"),
        "profession":req.POST.get("profession"),
        "followers":req.POST.get("followers"),
        "nationality":req.POST.get("nationality"),
        "DOB":req.POST.get("DOB")
    }
        profile_pic=req.FILES.get("profile_pic")
        if profile_pic:
          upload_pic=cloudinary.uploader.upload(profile_pic)
          profile_url=upload_pic["secure_url"]
        else:
           profile_url=None
        register_data["profile_pic"]=profile_url

        if Celebrities.objects.filter(name=register_data["name"]).exists():
           message="Celebrity already exists"
           return render(req,"register.html",{"message":message})
    
        serializer=CelebritySerializer(data=register_data)
        if serializer.is_valid():
           serializer.save()
           message="Registration sucessfully"
        # return JsonResponse({"msg":"Registration sucessfully"})
        else:
           message=serializer.errors
    return render(req,"register.html",{"message":message})
    
def update(req):
   message=""
   if req.method=="POST":
      name=req.POST.get("name")
      try:
         celeb=Celebrities.objects.get(name=name)
      except Celebrities.DoesNotExist:
         return JsonResponse({"error":"Celebrity not found"})
      
      update_data = {
            "name": name,
            "age": req.POST.get("age", celeb.age),
            "gender": req.POST.get("gender", celeb.gender),
            "profession": req.POST.get("profession", celeb.profession),
            "followers": req.POST.get("followers", celeb.followers),
            "nationality": req.POST.get("nationality", celeb.nationality),
            "DOB": req.POST.get("dob", celeb.DOB)
        }
      profile_pic=req.FILES.get("profile_pic")
      if profile_pic:
         upload=cloudinary.uploader.upload(profile_pic)
         celeb.profile_pic=upload["secure_url"]
      serializer = CelebritySerializer(celeb, data=update_data)
      if serializer.is_valid():
         serializer.save()
         message = "Celebrity updated successfully "
      else:
        message = serializer.errors
   return render(req,"update.html",{"message":message})


def delete(req):
   message=""
   if req.method=="POST":
      name=req.POST.get("name")
      try:
         celeb=Celebrities.objects.get(name=name)
         celeb.delete()
         message=f"Celebrity {name} deleted sucessfully"
      except Celebrities.DoesNotExist:
         message="celebrity not found"
   return render(req,"delete.html",{"message":message})



def get_data(req):
    all_data=Celebrities.objects.all()
    # serializer=CelebritySerializer(all_data,many=True)
    # return JsonResponse({"msg":serializer.data})
    return render(req,"data.html",{"celebrities":all_data})
    

def dashboard(req):
   return render(req,"Dashboard.html")