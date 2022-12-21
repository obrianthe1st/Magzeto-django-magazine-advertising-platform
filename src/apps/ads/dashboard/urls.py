
from django.contrib import admin
from django.urls import include, path

from .views import dashboard_view

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
] 