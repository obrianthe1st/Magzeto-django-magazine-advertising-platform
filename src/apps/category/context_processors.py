from datetime import datetime

from .models import Category


def menu_links(request):
    """
    Fetches all categories from the database.

    Args:
        request (_type_): dictionary

    returns:
    dictionary of category links from the category table
    """
    time_now=datetime.strftime(datetime.now(),"%A, %B %d, %Y")
    
    category_links = Category.objects.prefetch_related()
    
    return dict(category_links=category_links,time=time_now)