from django.db import models

# Create your models here.

class SearchAd(models.Model):
    campaign_id = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    link = models.URLField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'search_ad'
        verbose_name_plural = 'search_ads'
        ordering = ['-created']

    def __str__(self):
        return self.title

class SponsoredAd(models.Model):
    
    campaign_id = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    link = models.URLField(max_length=150)
    image = models.ImageField(upload_to='sponsored/',default='default/sponsored_ad.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'sponsored_ad'
        verbose_name_plural = 'sponsored_ads'
        ordering = ['-created']

    def __str__(self):
        return self.title