from django.contrib import admin
from django.urls import path
from app2 import views
urlpatterns = [
    path('app2/',views.display),
]
