from django.urls import path
from . import views

urlpatterns=[
    path("get_user/",views.get_users),
    # path("reg_user/",views.reg_user),
    # path("update_user/",views.update_user),
    # path("delete_user/",views.delete_user)

]