from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def dashboard_view(request):
    context={}
    return render(request,'ads/dashboard.html',context)


def helloWorld(request):
    return JsonResponse({'text':'hello world'})
