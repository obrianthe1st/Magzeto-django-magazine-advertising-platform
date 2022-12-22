from django.shortcuts import render

# Create your views here.

def campaign_home(request):
    context={}
    return render(request,'ads/campaigns/campaign_home.html',context) 
