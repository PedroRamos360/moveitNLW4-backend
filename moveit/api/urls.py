from django.urls import path
from .views import *

urlpatterns = [
    path('get-user/<str:username>', GetUser.as_view()),
    path('create-user', CreateUser.as_view()),
    path('update-user', UpdateUser.as_view())
]