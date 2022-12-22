from django.urls import path

from .views import campaign_home

urlpatterns = [
    path('',campaign_home,name='campaign_home'),
    
]
