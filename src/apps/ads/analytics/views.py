from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ads.advert.models import SearchAd, SponsoredAd

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
        SponsoredAdImpression.objects.bulk_create([SponsoredAdImpression(advertisement_name=ad.title,sponsored_ad_id=ad.id)])

def search_ads_impression_counter(request):
    current_search_page_ads = searchPageAds()
    for ad in current_search_page_ads:
        SearchAdImpression.objects.bulk_create([SearchAdImpression(advertisement_name=ad.title,searchad_id=ad.id)])
        
def sponsored_ad_view(request,sponsored_ad_id=None):

    try:
        sponsored_ad = SponsoredAd.objects.get(id=sponsored_ad_id)
    except SponsoredAd.DoesNotExist as e:
        raise e

    SponsoredAdClicks.objects.bulk_create([SponsoredAdClicks(advertisement_name=sponsored_ad.title,sponsored_ad_id=sponsored_ad.id)])


    return redirect(sponsored_ad.link)


def search_ad_view(request,searchad_id=None):

    try:
        search_ad = SearchAd.objects.get(id=searchad_id)
    except SearchAd.DoesNotExist as e:
        raise e

    SearchAdClicks.objects.bulk_create([SearchAdClicks(advertisement_name=search_ad.title,searchad_id=search_ad.id)])


    return redirect(search_ad.link)

    




