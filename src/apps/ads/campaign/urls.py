from django.urls import path

from .views import (
    campaign_billing,
    campaign_billing_setup,
    campaign_goal,
    campaign_home,
    campaign_search_ad_view,
    campaign_search_settings_view,
    campaign_sponsored_ad_view,
    campaign_sponsored_settings_view,
    campaign_type,
)

app_name="campaigns"

urlpatterns = [
    path('',campaign_home,name='campaign_home'),
    path('goal/',campaign_goal,name='campaign_goal'),
    path('goal/type/',campaign_type,name='campaign_type'),
    path('goal/type/search_settings/',campaign_search_settings_view,name='campaign_search_settings'),  
    path('goal/type/sponsored_settings/',campaign_sponsored_settings_view,name='campaign_sponsored_settings'),   
    path('goal/type/search_settings/create_search_ad/',campaign_search_ad_view,name="create_search_ad"),
    path('goal/type/sponsored_settings/create_sponsored_ad/',campaign_sponsored_ad_view,name="create_sponsored_ad"),
    path('billing/',campaign_billing,name='campaign_billing'),
    path('billing/setup/',campaign_billing_setup,name='campaign_billing_setup'),
    

]
