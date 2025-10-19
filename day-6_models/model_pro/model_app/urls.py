from django.urls import path
from . import views

urlpatterns=[
    path("details/",views.details),
    path("reg_user/",views.reg_user)
]