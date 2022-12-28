import datetime
from datetime import date
from datetime import datetime as Datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.db.models import Count, DateTimeField, QuerySet, Sum
from django.db.models.functions import Trunc, TruncDate, TruncDay, TruncMonth, TruncWeek
from django.utils.timezone import make_aware

from apps.ads.analytics.models import (
    SearchAdClicks,
    SearchAdImpression,
    SponsoredAdClicks,
    SponsoredAdImpression,
)
from apps.ads.campaign.models import (
    SearchAd,
    SearchCampaign,
    SponsoredAd,
    SponsoredCampaign,
)

#use date range as well
#use strptime to get the month as well
# I am gonna have each function that handles a particular chart

dates = datetime.datetime.now() - relativedelta(months=12)   
dates = datetime.datetime.now() - relativedelta(days=7)    


def get_campaigns_data(request):
    campaign_list = []

    search_campaigns = SearchCampaign.objects.filter(campaign_manager=request.user)
    sponsored_campaigns = SponsoredCampaign.objects.filter(campaign_manager=request.user)
    
    if search_campaigns:
        for each_campaign in search_campaigns:
            campaign_list.append(each_campaign)

    if sponsored_campaigns:
        for each_campaign in sponsored_campaigns:
            campaign_list.append(each_campaign)

    return campaign_list

def get_ad_data(campaigns=None):
    ads_list =  []


    for each_campaign in campaigns:
        if isinstance(each_campaign,SponsoredCampaign):
            sponsored_ads = SponsoredAd.objects.filter(campaign_id=each_campaign.id)
            ads_list.append(sponsored_ads)

        if isinstance(each_campaign,SearchCampaign):
            search_ads = SearchAd.objects.filter(campaign_id=each_campaign.id)
            ads_list.append(search_ads)
    return ads_list

def get_ad_analytics_data(request,campaign_data=None):
    clicks_data = []
    impressions_data = []
    advert_ids = set()
    
    for each_campaign in campaign_data:
        if isinstance(each_campaign,QuerySet):
            for each_ad in each_campaign:
                advert_ids.add(each_ad.id)
 

    search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:7]

    if search_ad_clicks:
        for each_data in search_ad_clicks:
            print(each_data["date"].strftime("%A"),each_data['clicks'])
        print("search ad clicks",search_ad_clicks)

    search_ad_impressions = SearchAdImpression.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('-date')[:7]

    if search_ad_impressions:
        print("search ad impressions",search_ad_impressions)
    
    sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:7]
    
    if sponsored_ad_clicks:
        print("sponsored ad clicks",sponsored_ad_clicks)

    sponsored_ad_impressions = SponsoredAdImpression.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('-date')[:7]


    if sponsored_ad_impressions:
        print("sponsored ad impressions",sponsored_ad_impressions)

    sponsored_ad_impressions_month = SponsoredAdImpression.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('date')[6:]

    if sponsored_ad_impressions_month:
        print("sponsored ad impressions for december",sponsored_ad_impressions_month)

    return (clicks_data,impressions_data)                    

                


def week_day_chart(dataset):
    pass