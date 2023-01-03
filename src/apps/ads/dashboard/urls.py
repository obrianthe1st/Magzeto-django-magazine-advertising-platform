
from django.contrib import admin
from django.urls import include, path

from .views import dashboard_view, helloWorld

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
    path('hello/',helloWorld,name='hello_world'),
] 