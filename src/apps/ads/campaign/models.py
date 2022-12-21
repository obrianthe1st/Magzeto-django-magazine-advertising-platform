from django.db import models

from apps.ads.ad.models import SearchAd, SponsoredAd
from apps.ads.billing.models import Billing
from apps.authors.models import Author

# Create your models here.

class Campaign(models.Model):
    campaign_manager = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    campaign_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.FloatField()
    billing = models.ForeignKey(Billing,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'campaign'
        verbose_name_plural = 'campaigns'
        ordering = ['-created']

    def __str__(self):
        return self.name

class SearchCampaign(Campaign):
    ad = models.ForeignKey(SearchAd,on_delete=models.SET_NULL,null=True)

class SponsoredCampaign(Campaign):
    ad = models.ForeignKey(SponsoredAd,on_delete=models.SET_NULL,null=True)


