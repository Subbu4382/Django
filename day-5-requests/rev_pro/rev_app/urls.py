from django.urls import path
from . import views

urlpatterns=[
    path("rev/",view=views.rev)
]