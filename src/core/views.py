import logging

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from apps.ads.analytics.utils import display_ads
from apps.ads.analytics.views import (
    search_ads_impression_counter,
    sponsored_ads_impression_counter,
)
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

    # sponsored_ads_impression_counter(request)
    home_page_ads = display_ads.homePageSponsoredAds()


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
               "politics_articles_2": politics_articles_2,
               "home_page_ads":home_page_ads}


    return render(request,'home.html',context)


def search_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    # search_ads_impression_counter(request)
    search_page_ads = display_ads.searchPageAds()

    articles = None

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            articles = Article.objects.filter(Q(title__icontains=keyword))
            if articles is None:
                articles = Article.objects.filter(Q(posts__icontains=keyword))

    context={
        'articles':articles,
        'keyword':keyword,
        'search_ads': search_page_ads,
    }

    return render(request,'search.html',context)