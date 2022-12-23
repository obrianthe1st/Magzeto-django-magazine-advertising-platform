from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ads.advert.models import SearchAd, SponsoredAd
from apps.ads.billing.models import Billing

from .forms import (
    BillingForm,
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
            request.session['campaign_id'] = search_campaign_settings.id
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
            request.session['campaign_id'] = sponsored_campaign_settings.id
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
  

    context = {}
    sponsored_ad_form = modelformset_factory(SponsoredAd,max_num=2,extra=2,fields=('title','description','link','image',))
    sponsoredAdForm = sponsored_ad_form(request.POST or None,request.FILES or None,queryset=SponsoredAd.objects.none())

    if request.method == 'POST':
        if sponsoredAdForm.is_valid():
            instances = sponsoredAdForm.save(commit=False)
            for each_ad in instances:
                each_ad.campaign_id = request.session.get('campaign_id')
                each_ad.save()
            return redirect('campaign_billing') #redirect to billing
        else:
            context = {"form":sponsoredAdForm,"type":"sponsored"}
            return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing
    else:
        context = {"form":sponsoredAdForm,"type":"sponsored"}
        return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing




@login_required()
def campaign_search_ad_view(request):

    context = {}
    search_ad_form = modelformset_factory(SearchAd,max_num=2,extra=2,fields=('title','description','link',))
    searchAdForm = search_ad_form(request.POST or None,queryset=SearchAd.objects.none())

    if request.method == 'POST':
        if searchAdForm.is_valid():
            instances = searchAdForm.save(commit=False)
            for each_ad in instances:
                each_ad.campaign_id = request.session.get('campaign_id')
                each_ad.save()
            return redirect('campaign_billing') #redirect to billing
        else:
            context = {"form":searchAdForm,"type":"search"}
            return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing

    else:
        context = {"form":searchAdForm,"type":"search"}
        return render(request,'ads/campaigns/create_ad.html',context) #redirect to billing



@login_required()
def campaign_billing(request):
    billing = Billing.objects.filter(card_holder=request.user).count()
    context={}

    if billing:
        if request.method == "POST":
            if request.session.has_key('campaign_id'):
                if SearchCampaign.objects.filter(id=request.session.get('campaign_id')).exists():
                    search_campaign = SearchCampaign.objects.get(id=request.session.get('campaign_id'))
                    search_campaign.active = True
                    search_campaign.save()
                    del request.session['campaign_id']
                    return redirect("dashboard")
                elif SponsoredCampaign.objects.filter(id=request.session.get('campaign_id')).exists():
                    sponsored_campaign = SponsoredCampaign.objectsget(id=request.session.get('campaign_id'))
                    sponsored_campaign.active = True
                    sponsored_campaign.save()
                    del request.session['campaign_id']
                    return redirect("dashboard")
        else:
            return render(request,'ads/campaigns/billing.html',context)
    else:
        return render(request,'ads/campaigns/no_billing.html',context)

@login_required()
def campaign_billing_setup(request):
    context={}
    if request.method == 'POST':
        billing_form = BillingForm(request.POST or None)
        if billing_form.is_valid():
            billing = Billing()
            billing.card_holder =  request.user
            billing.card_holder_name = billing_form.cleaned_data['card_holder_name']
            billing.card_number = billing_form.cleaned_data['card_number']
            billing.country = billing_form.cleaned_data['country']
            billing.month = billing_form.cleaned_data['month']
            billing.day = billing_form.cleaned_data['day']
            billing.cvc = billing_form.cleaned_data['cvc']
            billing.save()
            return redirect("dashboard")
        else:
            form = BillingForm()
            context={"form":form}
            return render(request,'ads/campaigns/billing_setup.html',context)
    else:
        form = BillingForm()
        context={"form":form}
        return render(request,'ads/campaigns/billing_setup.html',context)
        

