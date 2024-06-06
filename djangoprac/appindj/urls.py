from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.app_in_dj, name="app_in_dj"),
]
