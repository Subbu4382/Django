from django.urls import path
from . import views

urlpatterns=[
    path("users/",views.users),
    path("reg_user/",views.reg_user)
]