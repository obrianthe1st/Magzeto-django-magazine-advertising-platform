import logging

from django.http import HttpResponse
from django.shortcuts import render

from apps.article.models import Article
from apps.article.utils import (
    display_around_the_world_articles_1,
    display_around_the_world_articles_2,
    display_latest_stories_articles,
    display_political_articles_1,
    display_political_articles_2,
    display_top_news_articles,
)
from apps.category.models import Category

from .tasks import add

#get the logger by name
#logger = logging.getLogger('main')

# Create your views here.

def test_celery(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    #add.delay()
    #logger.info("something is wrong with my db problem")
    return HttpResponse("<body>Done</body>")

def home_view(request):
    """
    Displays the view for the home page.

    Args:
        request (_type_): _description_
    """

    top_articles = display_top_news_articles(request)
    around_the_world_1 = display_around_the_world_articles_1(request)
    around_the_world_2 = display_around_the_world_articles_2(request)
    latest_articles = display_latest_stories_articles(request)
    politics_articles_1= display_political_articles_1(request)
    politics_articles_2= display_political_articles_2(request)



    context = {"top_articles":top_articles, 
               "around_the_world_1":around_the_world_1,
               "around_the_world_2":around_the_world_2,
               "latest_articles":latest_articles,
               "politics_articles_1": politics_articles_1,
               "politics_articles_2": politics_articles_2,}


    return render(request,'home.html',context)

