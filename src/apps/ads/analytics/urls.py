from django.urls import path

from .views import search_ad_view, sponsored_ad_view

urlpatterns = [
    path("<int:sponsored_ad_id>/",sponsored_ad_view,name="sponsored_ad"),
    path("search/<int:searchad_id>/",search_ad_view,name="search_ad"),

    
]
