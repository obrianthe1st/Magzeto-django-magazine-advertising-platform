from django.urls import path

from .views import campaign_goal, campaign_home, campaign_settings_view, campaign_type

urlpatterns = [
    path('',campaign_home,name='campaign_home'),
    path('goal/',campaign_goal,name='campaign_goal'),
    path('goal/type/',campaign_type,name='campaign_type'),
    path('goal/type/settings/',campaign_settings_view,name='campaign_settings'),   
]
