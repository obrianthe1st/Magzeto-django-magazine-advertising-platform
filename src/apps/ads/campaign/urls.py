from django.urls import path

from .views import (
    campaign_goal,
    campaign_home,
    campaign_search_settings_view,
    campaign_sponsored_settings_view,
    campaign_type,
)

urlpatterns = [
    path('',campaign_home,name='campaign_home'),
    path('goal/',campaign_goal,name='campaign_goal'),
    path('goal/type/',campaign_type,name='campaign_type'),
    path('goal/type/search_settings/',campaign_search_settings_view,name='campaign_search_settings'),  
    path('goal/type/sponsored_settings/',campaign_sponsored_settings_view,name='campaign_sponsored_settings'),   
]
