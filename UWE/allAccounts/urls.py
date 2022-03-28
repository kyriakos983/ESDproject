from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login,name='login'),
    path('register_user', views.register_user,name='register'),
]
