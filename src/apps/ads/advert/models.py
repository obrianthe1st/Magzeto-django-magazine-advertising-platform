from django.db import models


class Advert(models.Model):

    campaign_id = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    link = models.URLField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name= 'advert'
        ordering = ['-created']
    
    def __str__(self):
        return self.title


class SearchAd(Advert):


    class Meta:
        verbose_name = 'search_ad'


class SponsoredAd(Advert):
      
    image = models.ImageField(upload_to='sponsored/',default='default/sponsored_ad.jpg')

    class Meta:
        verbose_name = 'sponsored_ad'