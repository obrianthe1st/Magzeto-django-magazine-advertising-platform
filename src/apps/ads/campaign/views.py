from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ads.advert.models import SearchAd, SponsoredAd

from .forms import (
    CreateSearchAdForm,
    CreateSponsoredAdForm,
    SearchCampaignForm,
    SponsoredCampaignForm,
)
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
            return redirect('create_search_ad')
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
            return redirect('create_sponsored_ad')
        else:
            form = SponsoredCampaignForm()  
            context = {'type':'sponsored','form':form}
            return render(request,'ads/campaigns/campaign_settings.html',context)
    else:
        form = SponsoredCampaignForm()  
        context = {'type':'sponsored','form':form}
        return render(request,'ads/campaigns/campaign_settings.html',context)


@login_required()
def campaign_sponsored_ad_view(request):
    sponsored_campaign = SponsoredCampaign.objects.filter(campaign_manager=request.user,active=False,campaign_type='sponsored').latest('created')

    context = {}
    sponsored_ad_form = modelformset_factory(SponsoredAd,max_num=2,extra=2,fields=('title','description','link','image',))
    sponsoredAdForm = sponsored_ad_form(request.POST or None,request.FILES or None,queryset=SponsoredAd.objects.none())

    if request.method == 'POST':
        if sponsoredAdForm.is_valid():
            instances = sponsoredAdForm.save(commit=False)
            for each_ad in instances:
                each_ad.campaign_id = sponsored_campaign.id
                each_ad.save()
            return redirect('create_sponsored_ad') #redirect to billing
        else:
            context = {"form":sponsoredAdForm,"type":"sponsored"}
            return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing
    else:
        context = {"form":sponsoredAdForm,"type":"sponsored"}
        return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing




@login_required()
def campaign_search_ad_view(request):
    search_campaign = SearchCampaign.objects.filter(campaign_manager=request.user,active=False,campaign_type='search').latest('created')

    context = {}
    search_ad_form = modelformset_factory(SearchAd,max_num=2,extra=2,fields=('title','description','link',))
    searchAdForm = search_ad_form(request.POST or None,queryset=SearchAd.objects.none())

    if request.method == 'POST':
        if searchAdForm.is_valid():
            instances = searchAdForm.save(commit=False)
            for each_ad in instances:
                each_ad.campaign_id = search_campaign.id
                each_ad.save()
            return redirect('create_search_ad') #redirect to billing
        else:
            context = {"form":searchAdForm,"type":"search"}
            return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing

    else:
        context = {"form":searchAdForm,"type":"search"}
        return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing

