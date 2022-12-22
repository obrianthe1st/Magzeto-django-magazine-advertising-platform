from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CampaignForm


# Create your views here.
@login_required()
def campaign_home(request):
    context={}
    return render(request,'ads/campaigns/campaign_home.html',context) 

@login_required()
def campaign_goal(request):
    context={}
    return render(request,'ads/campaigns/campaign_goal.html',context) 

@login_required()
def campaign_type(request):
    context={}
    return render(request,'ads/campaigns/campaign_type.html',context) 

@login_required()
def campaign_settings_view(request):
    form = CampaignForm(request.POST or None)
    pass
