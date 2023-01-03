from django.db import models

from apps.ads.advert.models import SearchAd, SponsoredAd

# Create your models here.

class SearchAdImpression(models.Model):
    advertisement_name = models.CharField(max_length=50,blank=True) 
    time_stamp =  models.DateField()
    searchad_id = models.IntegerField()
    impressions = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SearchAdImpression'
        verbose_name_plural = 'SearchAdImpressions'
        ordering = ('created',)

    def __str__(self):
        return self.advertisement_name
        # return self.advertisement_name + ' ' + self.campaign_name




class SearchAdClicks(models.Model):
    advertisement_name = models.CharField(max_length=50,blank=True) 
    time_stamp =  models.DateField()
    searchad_id = models.IntegerField()
    cpc = models.FloatField(null=True)
    clicks = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SearchAdClick'
        verbose_name_plural = 'SearchAdClicks'
        ordering = ('created',)

    def __str__(self):
        return self.advertisement_name


class SponsoredAdImpression(models.Model):
    advertisement_name = models.CharField(max_length=50,blank=True) 
    time_stamp =  models.DateField()
    sponsored_ad_id = models.IntegerField()
    impressions = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SponsoredAdImpression'
        verbose_name_plural = 'SponsoredAdImpressions'
        ordering = ('created',)
     
    def __str__(self):
        return self.advertisement_name


class SponsoredAdClicks(models.Model):
    advertisement_name = models.CharField(max_length=50,blank=True) 
    time_stamp =  models.DateField()
    sponsored_ad_id = models.IntegerField()
    cpc = models.FloatField(null=True)
    clicks = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'SponsoredAdClick'
        verbose_name_plural = 'SponsoredAdClicks'
        ordering = ('created',)

    def __str__(self):
        return self.advertisement_name
