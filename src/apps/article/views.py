from django.shortcuts import render

from apps.category.models import Category

from .models import Article


# Create your views here.
def article_view(request,category_slug=None,article_slug=None):
   


    try:
        article = Article.objects.get(slug=article_slug)
    except Article.DoesNotExist as e:
        raise e

    all_tags = article.tag.all()


    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist as e:
        raise e



    context={"article":article,"category":category,"tags":all_tags}

    return render(request,'article.html',context);