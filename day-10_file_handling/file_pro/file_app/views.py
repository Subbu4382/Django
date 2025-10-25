from django.shortcuts import render
import re
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


def validate_file(file_obj):
    # Check file size (limit 5MB)
    max_size = 5 * 1024 * 1024
    if file_obj.size > max_size:
        return False, 'File too large. Max size is 5MB.'

    # Check content type (MIME)
    allowed_types = ['image/jpeg', 'image/png']
    if file_obj.content_type not in allowed_types:
        return False, 'Invalid file type. Allowed: JPG, PNG'
    
    
      
    return True, 'Valid file'

@csrf_exempt
def register_user(request):
        # Get form fields
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        profile_picture = request.FILES.get("profile_picture")


        # Validate Name
        if not name or len(name) < 10 or len(name) > 25:
            return HttpResponse("Name must be between 20 to 25 characters")
        
        # Validate Email
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email or not re.match(email_pattern, email):
            return HttpResponse(" Enter a valid email address")

       
        # Validate Phone Number (Indian)
      
        phone_pattern = r'^[6-9]\d{9}$'   # starts with 6-9, 10 digits total
        if not phone or not re.match(phone_pattern, phone):
            return HttpResponse("Enter a valid Indian phone number (10 digits)")

        
        # Validate Profile Picture
        if not profile_picture:
            return HttpResponse("Profile picture is required")

        
        is_valid, message = validate_file(profile_picture)
        if not is_valid:
            return HttpResponse(message)
        # Save Valid Data to Database
        
        user = User.objects.create(
            name=name,
            email=email,
            phone=phone,
            profile_picture=profile_picture
        )
        return HttpResponse(f" User {user.name} registered successfully!")
