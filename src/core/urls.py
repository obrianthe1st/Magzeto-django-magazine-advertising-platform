
from django.urls import path

from apps.article.views import article_view
from apps.category.views import category_view

from .views import home_view, search_view, test_celery

urlpatterns = [
     #path('', test_celery, name="celery_view"),
     path('',home_view,name='home_view'),
     path('category/<slug:category_slug>/',category_view,name='category'),
     path('article/<slug:category_slug>/<slug:article_slug>/',article_view,name='article'),
     path('search/',search_view,name='search'),
]
