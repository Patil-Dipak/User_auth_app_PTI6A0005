from django.urls import path
from .views import *

app_name = "authapp"

urlpatterns = [
     path('register/', register, name='register'),
]