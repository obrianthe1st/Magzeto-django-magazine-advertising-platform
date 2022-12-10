import logging

from django.http import HttpResponse
from django.shortcuts import render

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

