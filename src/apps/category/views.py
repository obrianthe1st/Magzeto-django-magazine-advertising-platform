from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from apps.article.models import Article
from apps.category.models import Category

# Create your views here.

def category_view(request,category_slug=None):
    category = None
    articles = None
    
    category = Category.objects.get(slug=category_slug) 
    articles = Article.objects.filter(category__slug=category)

    if articles is not None:
        paginator = Paginator(articles,6)
        page = request.GET.get('page')
        paged_articles = paginator.get_page(page)
    else:
        return render(request,'category.html',context)
    
    context = {'articles':paged_articles,'category':category}
    return render(request,'category.html',context)

    
    
