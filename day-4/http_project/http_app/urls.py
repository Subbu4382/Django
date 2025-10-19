from django.urls import path ## For defining the app urls
from . import views

urlpatterns=[
   path('welcome/', views.welcome, name='welcome'),
   path("details/",views.details_view),
   path("details/<int:id>",views.single_user),
   path("register/",views.register_user)
]