from django.db.models import Q

from .models import Article


def display_top_news_articles(request):
    top_articles = Article.objects.filter(Q(title__contains='Trump') |
     Q(title__contains='Democrat'))[:3]
    return top_articles

def display_political_articles_1(request):
    political_articles_1 = Article.objects.filter(category__name='politics')[:2]
    return political_articles_1

def display_political_articles_2(request):
    political_articles_2 = Article.objects.filter(category__name='politics')[2:4]
    return political_articles_2


def display_around_the_world_articles_1(request):
    around_the_world_articles_1 = Article.objects.exclude(category__name='politics')[:3]
    return around_the_world_articles_1



def display_around_the_world_articles_2(request):
    around_the_world_articles_2 = Article.objects.exclude(category__name='politics')[3:6]
    return around_the_world_articles_2
    

def display_latest_stories_articles(request):
    lastest_stories_articles = Article.objects.all().order_by('-created')[:4]
    return lastest_stories_articles