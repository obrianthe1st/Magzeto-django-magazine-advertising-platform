import datetime
from collections import OrderedDict
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


def get_search_ad_clicks_data(request,days=None,month=None,campaign_data=None):

    advert_ids = get_advert_ids(campaign_data=campaign_data)
    
    if month is None:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:days]
    else:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('date')[month:]

    
    if search_ad_clicks:
        for each_data in search_ad_clicks:
            print(each_data["date"].strftime("%B"),each_data['clicks'])
        print("search ad clicks",len(search_ad_clicks))



def get_spend_data(request,days=None,month=None,campaign_data=None):
    advert_ids = get_advert_ids(campaign_data=campaign_data)

    ad_data = {'search_ad':[],'sponsored_ad':[]}
    spend_data = {"date":[],"spend":[]}
    
    if month is None:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:days]

        sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:days]
    else:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('date')[month:]

        sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('date')[month:]


    for each_ad in search_ad_clicks:
        if month is None:
            ad_data['search_ad'].append((each_ad["date"].strftime('%-d %B'),each_ad["clicks"],))
        else:
            ad_data['search_ad'].append((each_ad["date"].strftime('%B'),each_ad["clicks"],))


    for each_ad in sponsored_ad_clicks:
        if month is None:
            ad_data['sponsored_ad'].append((each_ad["date"].strftime('%-d %B'),each_ad["clicks"],))
        else:
            ad_data['sponsored_ad'].append((each_ad["date"].strftime('%B'),each_ad["clicks"],))

    for k,v in zip(ad_data['search_ad'],ad_data['sponsored_ad']):
        spend_data["date"].append(k[0])
        spend_data["spend"].append(round((k[1] * 0.1) + (v[1] * 0.1),2))


    return dict(spend_data)

def get_impressions_data(request,days=None,month=None,campaign_data=None):
    advert_ids = get_advert_ids(campaign_data=campaign_data)

    impression_data = {'search_impression':[],'sponsored_impression':[]}
    impressions = {"date":[],"impressions":[]}

    if month is None:
        search_ad_impressions = SearchAdImpression.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('-date')[:days]

        sponsored_ad_impressions = SponsoredAdImpression.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('-date')[:days]
    else:
        search_ad_impressions = SearchAdImpression.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('date')[month:]

        sponsored_ad_impressions = SponsoredAdImpression.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(impressions=Sum('impressions')).order_by('date')[month:]

    for each_ad in search_ad_impressions:
        if month:
            impression_data['search_impression'].append((each_ad["date"].strftime('%B'),each_ad["impressions"],))
        else:
            impression_data['search_impression'].append((each_ad["date"].strftime('%-d %B'),each_ad["impressions"],))



    for each_ad in sponsored_ad_impressions:
        if month:
            impression_data['sponsored_impression'].append((each_ad["date"].strftime('%B'),each_ad["impressions"],))
        else:
            impression_data['sponsored_impression'].append((each_ad["date"].strftime('%-d %B'),each_ad["impressions"],))

    for k,v in zip(impression_data['search_impression'],impression_data['sponsored_impression']):
        impressions["date"].append(k[0])
        impressions["impressions"].append(round((k[1] * 0.1) + (v[1] * 0.1),2))

    return dict(impressions)


def get_clicks_data(request,days=None,month=None,campaign_data=None):
    advert_ids = get_advert_ids(campaign_data=campaign_data)

    clicks_data = {'search_clicks':[],'sponsored_clicks':[]}
    clicks = {"date":[],"clicks":[]}

    if month is None:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:days]

        sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncDate('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('-date')[:days]
    else:
        search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('date')[month:]

        sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).order_by().annotate(date=TruncMonth('time_stamp')).values('date').annotate(clicks=Sum('clicks')).order_by('date')[month:]

    for each_ad in search_ad_clicks:
        clicks_data['search_clicks'].append((each_ad["date"],each_ad["clicks"],))

    for each_ad in sponsored_ad_clicks:
        clicks_data['sponsored_clicks'].append((each_ad["date"],each_ad["clicks"],))

    for k,v in zip(clicks_data['search_clicks'],clicks_data['sponsored_clicks']):
        clicks["date"].append(k[0])
        clicks["clicks"].append(round((k[1] * 0.1) + (v[1] * 0.1),2))

    return dict(clicks)

def impressions_VS_clicks_data(request,days=None,month=None,campaign_data=None):
    clicks_impressions_data = []

    if month is None:
        clicks = get_clicks_data(request,days=days,campaign_data=campaign_data)
        impressions = get_impressions_data(request,days=days,campaign_data=campaign_data)
    else:
        clicks = get_clicks_data(request,month=month,campaign_data=campaign_data)
        impressions = get_impressions_data(request,month=month,campaign_data=campaign_data)

    return(dict(clicks),dict(impressions))

def top_3_performing_campaigns(request):
    performing_campaigns = {}
    top_3_performing_campaigns = []
    campaign_s = get_campaigns_data(request)
    campaign_data = get_ad_data(campaigns=campaign_s)

    advert_ids = get_advert_ids(campaign_data=campaign_data)

    search_ad_clicks = SearchAdClicks.objects.filter(searchad_id__in=advert_ids).values('searchad_id').annotate(clicks=Sum('clicks')).order_by('searchad_id')

    search_ad_impressions = SearchAdImpression.objects.filter(searchad_id__in=advert_ids).values('searchad_id',).annotate(impressions=Sum('impressions')).order_by('searchad_id')

    sponsored_ad_clicks = SponsoredAdClicks.objects.filter(sponsored_ad_id__in=advert_ids).values('sponsored_ad_id').annotate(clicks=Sum('clicks')).order_by('sponsored_ad_id')

    sponsored_ad_impressions = SponsoredAdImpression.objects.filter(sponsored_ad_id__in=advert_ids).values('sponsored_ad_id').annotate(impressions=Sum('impressions')).order_by('sponsored_ad_id')

    for ad1, ad2 in zip(search_ad_clicks,search_ad_impressions):
        performing_campaigns[get_campaign_name(ad1['searchad_id'])] = {
        'spend':round((ad1['clicks'] * 0.01),2),'CTR':round(((ad1['clicks'] / ad2['impressions']) * 100),2)}


    for ad1, ad2 in zip(sponsored_ad_clicks,sponsored_ad_impressions):
        performing_campaigns[get_campaign_name(ad1['sponsored_ad_id'])] = {
        'spend':round((ad1['clicks'] * 0.01),2),'CTR':round(((ad1['clicks'] / ad2['impressions']) * 100),2)}

    sorted_campaigns = OrderedDict(sorted(performing_campaigns.items(), key=lambda x: x[1]['CTR']))
    
    if len(sorted_campaigns) < 3:
        return sorted_campaigns
    else:
        for i in range(0,3):
            top_3_performing_campaigns.append((list(sorted_campaigns.keys())[i],list(sorted_campaigns.values())[i]))
        return dict(top_3_performing_campaigns)


def get_campaign_name(ad_id=None):
    """
    Gets campaign name based on id
    """
    campaign_name = None

    ads = SearchAd.objects.filter(id=ad_id)
    if ads:
        campaign = SearchCampaign.objects.filter(id=ads[0].campaign_id)
        campaign_name = campaign[0].name
    else:
        ads = SponsoredAd.objects.filter(id=ad_id)
        campaign = SponsoredCampaign.objects.filter(id=ads[0].campaign_id)
        campaign_name = campaign[0].name
    return campaign_name



def get_advert_ids(campaign_data=None):

    advert_ids = set()
    for each_campaign in campaign_data:
        if isinstance(each_campaign,QuerySet):
            for each_ad in each_campaign:
                advert_ids.add(each_ad.id)

    return advert_ids
 
#Look at if I miss days as well for clicks
#put it into a function as well, put everything in readable format for json
