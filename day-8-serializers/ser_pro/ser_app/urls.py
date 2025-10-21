from django.urls import path
from . import views


urlpatterns=[
    path("update_user/<int:id>",views.update_user),
    path("delete_user/<int:id>",views.delete_user),
    path("get_users/",views.get_users),
    path("create_user/",views.create_user),
]

