
from django.contrib import admin
from django.urls import include, path

from .views import dashboard_view, helloWorld, showAnalyticsData

urlpatterns = [
    path('',dashboard_view,name='dashboard'),
    path('hello/',helloWorld,name='hello_world'),
    path('show_analytics/',showAnalyticsData,name='show_analytics')
] 