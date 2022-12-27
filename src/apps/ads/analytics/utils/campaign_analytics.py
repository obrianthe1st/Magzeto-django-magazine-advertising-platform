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

# print(Datetime.now() - datetime.timedelta(days=7))
# print(Datetime.now() - datetime.timedelta(days=30))
# print(Datetime.now() - datetime.timedelta(days=90))
# print(Datetime.now() - datetime.timedelta(days=180))
# print(Datetime.now() - datetime.timedelta(days=270))
# print(Datetime.now() - datetime.timedelta(days=360))

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
    search_ad_ids = set()
    # date_str = "\d{4}-\d{2}-\d{2}"
    # start_date = Datetime.now()
    # print(start_date)
    # end_date = start_date - datetime.timedelta(days=7)
    # print(end_date)
    start_date = '2022-12-26'
    # # end_date = '2022-12-27'
    
    for each_campaign in campaign_data:
        if isinstance(each_campaign,QuerySet):
            for each_ad in each_campaign:
                print(each_ad.id)
                # print(type(each_ad))
                # if isinstance(each_ad,SearchAd):
                #     search_ads = SearchAdClicks.objects.filter(searchad_id=each_ad.id)
                #     search_ad_ids.add(each_ad.id)

                #     sponsored_ads = SearchAdImpression.objects.filter(searchad_id=each_ad.id)
                #     search_ad_ids.add(each_ad.id)


    search_ad_clicks = SearchAdClicks.objects.order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks'))

    if search_ad_clicks:
        print(search_ad_clicks)

    search_ad_impressions = SearchAdImpression.objects.order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(impressions=Sum('impressions'))

    # if search_ad_impressions:
    #         print(search_ad_impressions)
    
                    # search_ad_clicks = SearchAdClicks.objects.filter(time_stamp__range=[start_date,end_date],advertisement_name=each_ad.title,searchad_id=each_ad.id)
                    # if search_ad_clicks:
                    #     clicks_data.append(search_ad_clicks)

                    # search_ad_impressions = SearchAdImpression.objects.filter(time_stamp__range=[start_date,end_date],advertisement_name=each_ad.title,searchad_id=each_ad.id)

                    # if search_ad_impressions:
                    #     impressions_data.append(search_ad_impressions)

                # if isinstance(each_ad,SponsoredAd):
                    
                #     sponsored_ad_clicks = SponsoredAdClicks.objects.filter(time_stamp__range=[start_date,end_date],advertisement_name=each_ad.title,sponsored_ad_id=each_ad.id)
                #     if sponsored_ad_clicks:
                #         print(sponsored_ad_clicks)

                #     sponsored_ad_impressions = SponsoredAdImpression.objects.filter(time_stamp__range=[start_date,end_date],advertisement_name=each_ad.title,sponsored_ad_id=each_ad.id)
                #     if sponsored_ad_impressions:
                #         impressions_data.append(sponsored_ad_impressions)

    return (clicks_data,impressions_data)                    

                


def week_day_chart(dataset):
    pass