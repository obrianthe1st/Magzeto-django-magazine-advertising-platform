from django.db import models

from apps.ads.advert.models import SearchAd, SponsoredAd

# Create your models here.

class SearchAdImpression(models.Model):
    advertisement = models.ForeignKey(SearchAd,on_delete=models.CASCADE)
    time_stamp =  models.DateTimeField(auto_now_add=True)
    searchad_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class SearchAdClicks(models.Model):
    advertisement = models.ForeignKey(SearchAd,on_delete=models.CASCADE)
    time_stamp =  models.DateTimeField(auto_now_add=True)
    searchad_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class SponsoredAdImpression(models.Model):
    advertisement = models.ForeignKey(SponsoredAd,on_delete=models.CASCADE)
    time_stamp =  models.DateTimeField(auto_now_add=True)
    sponsored_ad_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class SponsoredAdClicks(models.Model):
    advertisement = models.ForeignKey(SponsoredAd,on_delete=models.CASCADE)
    time_stamp =  models.DateTimeField(auto_now_add=True)
    sponsored_ad_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
