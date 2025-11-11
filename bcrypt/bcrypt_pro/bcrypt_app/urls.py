from django.urls import path
from . import views
urlpatterns=[
    path("reg_student/",views.reg_student),
    path("get_students/",views.get_students),
    path("login/",views.login)
]