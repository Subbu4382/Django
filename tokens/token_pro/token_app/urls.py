from django.urls import path
from . import views
urlpatterns=[
    path("reg_user/",views.reg_user),
    path("get_users/",views.get_users),
    path("update_user/",views.update_user),
    path("delete_user/",views.delete_user),
    path("login_user/",views.login_user)
]