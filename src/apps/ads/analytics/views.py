from datetime import date

from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ads.advert.models import SearchAd, SponsoredAd
from apps.ads.campaign.models import SearchCampaign, SponsoredCampaign

from .models import (
    SearchAdClicks,
    SearchAdImpression,
    SponsoredAdClicks,
    SponsoredAdImpression,
)
from .utils.display_ads import homePageSponsoredAds, searchPageAds

# Create your views here.

def sponsored_ads_impression_counter(request):
    current_home_page_ads = homePageSponsoredAds()
    for ad in current_home_page_ads:
        sponsored_impressions = SponsoredAdImpression.objects.filter(advertisement_name=ad.title,sponsored_ad_id=ad.id,time_stamp=date.today())

        if sponsored_impressions:
            sponsored_impressions[0].impressions += 1
            sponsored_impressions[0].save()
        else:
            SponsoredAdImpression.objects.create(advertisement_name=ad.title,sponsored_ad_id=ad.id,impressions=1,time_stamp=date.today())

def search_ads_impression_counter(request):
    current_search_page_ads = searchPageAds()
    if current_search_page_ads is None:
        return None
    for ad in current_search_page_ads:
        search_ad_impressions = SearchAdImpression.objects.filter(advertisement_name=ad.title,searchad_id=ad.id,time_stamp=date.today())

        if search_ad_impressions:
            search_ad_impressions[0].impressions += 1
            search_ad_impressions[0].save()
        else:
            SearchAdImpression.objects.create(advertisement_name=ad.title,searchad_id=ad.id,impressions=1,time_stamp=date.today())
  
        
def sponsored_ad_view(request,sponsored_ad_id=None):

    try:
        sponsored_ad = SponsoredAd.objects.get(id=sponsored_ad_id)
    except SponsoredAd.DoesNotExist as e:
        raise e

    try:
        campaign = SponsoredCampaign.objects.filter(id=sponsored_ad.campaign_id,active=True)
    except SponsoredCampaign.DoesNotExist as e:
        raise e

   
    sponsored_ad_clicks = SponsoredAdClicks.objects.filter(advertisement_name=sponsored_ad.title,sponsored_ad_id=sponsored_ad.id,time_stamp=date.today())
 

    if sponsored_ad_clicks:
        if (sponsored_ad_clicks[0].cpc * sponsored_ad_clicks[0].clicks) > campaign[0].budget:
                 campaign.active = False
                 campaign.save()
        else:
            sponsored_ad_clicks[0].clicks += 1
            sponsored_ad_clicks[0].save()
            return redirect(sponsored_ad.link)
    else:
        SponsoredAdClicks.objects.create(advertisement_name=sponsored_ad.title,sponsored_ad_id=sponsored_ad.id,cpc=0.10,clicks=1,time_stamp=date.today())
        return redirect(sponsored_ad.link)


def search_ad_view(request,searchad_id=None):

    # try:
    #     search_ad = SearchAd.objects.get(id=searchad_id)
    # except SearchAd.DoesNotExist as e:
    #     raise e

    # SearchAdClicks.objects.bulk_create([SearchAdClicks(advertisement_name=search_ad.title,searchad_id=search_ad.id)])


    # return redirect(search_ad.link)

    try:
        search_ad = SearchAd.objects.get(id=searchad_id)
    except SearchAd.DoesNotExist as e:
        raise e

    try:
        campaign = SearchCampaign.objects.filter(id=search_ad.campaign_id,active=True)
    except SearchCampaign.DoesNotExist as e:
        raise e

   
    search_ad_clicks = SearchAdClicks.objects.filter(advertisement_name=search_ad.title,searchad_id=search_ad.id,time_stamp=date.today())
 

    if search_ad_clicks:
        if (search_ad_clicks[0].cpc * search_ad_clicks[0].clicks) > campaign[0].budget:
                 campaign.active = False
                 campaign.save()
        else:
            search_ad_clicks[0].clicks += 1
            search_ad_clicks[0].save()
            return redirect(search_ad.link)
    else:
        SearchAdClicks.objects.create(advertisement_name=search_ad.title,searchad_id=search_ad.id,cpc=0.10,clicks=1,time_stamp=date.today())
        return redirect(search_ad.link)

