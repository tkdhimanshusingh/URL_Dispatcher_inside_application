from django.contrib import admin
from django.urls import path
from app4 import views
urlpatterns = [
    path('app4/',views.display),
]
