from django.urls import path
from . import views
urlpatterns=[
    path("",views.dashboard),
    path("dashboard/",views.dashboard),
    path("register/",views.register),
    path("get_data/",views.get_data),
    path("update/",views.update),
    path("delete/",views.delete),
    path("Alldata/",views.Alldata),
     path("data/<int:id>/",views.data)
]