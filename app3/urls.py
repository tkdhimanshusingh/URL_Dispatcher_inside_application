from django.contrib import admin
from django.urls import path
from app3 import views
urlpatterns = [
    path('app3/',views.display),
]
