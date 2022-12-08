from django.http import HttpResponse
from django.shortcuts import render

from .tasks import add

# Create your views here.

def test_celery(request):
    add.delay()
    return HttpResponse("Done")

