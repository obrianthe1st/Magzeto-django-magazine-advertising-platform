import random
import time
from datetime import date, datetime, timedelta

from django.core.management.base import BaseCommand

from apps.ads.analytics.models import (
    SearchAdClicks,
    SearchAdImpression,
    SponsoredAdClicks,
    SponsoredAdImpression,
)

ad_data = [{"title":"Everything seems fine","id":38,"type":"search"},
           {"title":"This is ad is good","id":37,"type":"search"},
           {"title":"Christmas ad 1", "id":16,"type":"sponsored"},
           {"title":"Jamaica is awesome","id":19,"type":"sponsored"},
           {"title":"Jamaica is great","id":18,"type":"sponsored"},
           {"title":"christmas ad 2", "id":17,"type":"sponsored"}]

# last_12_months = date.today() - timedelta(days=365)

def create_ad_data(days,delete=False):
    """
    Creates data for our analytics models. 

    Args:
        days (int): The number of days worth of data we want to insert into our database. 
        delete (bool, optional): If delete is True it will delete the database that was created prior and return. If it is False it will not delete the database. Defaults to False.
    """
    if delete:
        SearchAdClicks.objects.all().delete()
        SearchAdImpression.objects.all().delete()
        SponsoredAdClicks.objects.all().delete()
        SponsoredAdImpression.objects.all().delete()
        return
    else:
        for i in range(1,days):
            random_clicks =  random.randint(10,100)
            random_impressions = random.randint(1000,10000)

            time_stamp_date = date.today() - timedelta(days=i)

            SearchAdClicks.objects.bulk_create([
                SearchAdClicks(advertisement_name="Everything seems fine",searchad_id=38,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10),
                SearchAdClicks(advertisement_name="This is ad is good",searchad_id=37,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10
                )])

            SearchAdImpression.objects.bulk_create([
                SearchAdImpression(advertisement_name="Everything seems fine",time_stamp=time_stamp_date,impressions=random_impressions,searchad_id=38),
                SearchAdImpression(advertisement_name="This is ad is good",time_stamp=time_stamp_date,impressions=random_impressions,searchad_id=37)])

            SponsoredAdImpression.objects.bulk_create([
                SponsoredAdImpression(advertisement_name="Christmas ad 1",sponsored_ad_id=16,time_stamp=time_stamp_date,impressions=random_impressions),
                SponsoredAdImpression(advertisement_name="Jamaica is awesome",sponsored_ad_id=19,time_stamp=time_stamp_date,impressions=random_impressions),
                SponsoredAdImpression(advertisement_name="Jamaica is great",sponsored_ad_id=18,time_stamp=time_stamp_date,impressions=random_impressions),
                SponsoredAdImpression(advertisement_name="Christmas ad 2",sponsored_ad_id=17,time_stamp=time_stamp_date,impressions=random_impressions),
            ])

            SponsoredAdClicks.objects.bulk_create([
                SponsoredAdClicks(advertisement_name="Christmas ad 1",sponsored_ad_id=16,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10),
                SponsoredAdClicks(advertisement_name="Jamaica is awesome",sponsored_ad_id=19,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10),
                SponsoredAdClicks(advertisement_name="Jamaica is great",sponsored_ad_id=18,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10),
                SponsoredAdClicks(advertisement_name="Christmas ad 2",sponsored_ad_id=17,time_stamp=time_stamp_date,clicks=random_clicks,cpc=0.10),
            ])
    






class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_arguments('days',type=int,help='days that needs to be entered')

    def handle(self,*args,**options):
        create_ad_data(360,delete=True)
        self.stdout.write(self.style.SUCCESS("finished creating data"))