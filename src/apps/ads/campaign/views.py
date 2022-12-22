from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SearchCampaignForm, SponsoredCampaignForm
from .models import SearchCampaign, SponsoredCampaign


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
def campaign_search_settings_view(request):
    if request.method == "POST":
        form = SearchCampaignForm(request.POST or None)
        if form.is_valid():
            search_campaign_settings = SearchCampaign()
            search_campaign_settings.campaign_manager = request.user
            search_campaign_settings.name = form.cleaned_data['name']
            search_campaign_settings.start_date = form.cleaned_data['start_date']
            search_campaign_settings.end_date = form.cleaned_data['end_date']
            search_campaign_settings.budget = form.cleaned_data['budget']
            search_campaign_settings.save()
            return redirect('campaign_search_settings')
        else:
            form = SearchCampaignForm()  
            return render(request,'ads/campaigns/campaign_settings.html',context={"type":"search","form":form})
    else:
        form = SearchCampaignForm()  
        context = {'type':'search','form':form}
        return render(request,'ads/campaigns/campaign_settings.html',context)



@login_required()
def campaign_sponsored_settings_view(request):
    if request.method == "POST":
        form = SponsoredCampaignForm(request.POST or None)
        if form.is_valid():
            sponsored_campaign_settings = SponsoredCampaign()
            sponsored_campaign_settings.campaign_manager = request.user
            sponsored_campaign_settings.name = form.cleaned_data['name']
            sponsored_campaign_settings.start_date = form.cleaned_data['start_date']
            sponsored_campaign_settings.end_date = form.cleaned_data['end_date']
            sponsored_campaign_settings.budget = form.cleaned_data['budget']
            sponsored_campaign_settings.save()
            return redirect('campaign_sponsored_settings')
        else:
            form = SponsoredCampaignForm()  
            context = {'type':'sponsored','form':form}
            return render(request,'ads/campaigns/campaign_settings.html',context)
    else:
        form = SponsoredCampaignForm()  
        context = {'type':'sponsored','form':form}
        return render(request,'ads/campaigns/campaign_settings.html',context)


