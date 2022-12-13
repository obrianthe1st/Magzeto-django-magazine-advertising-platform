
from django.urls import path

from apps.category.views import category_view

from .views import home_view, test_celery

urlpatterns = [
     #path('', test_celery, name="celery_view"),
     path('',home_view,name='home_view'),
     path('<slug:category_slug>/',category_view,name='category_view'),
]
