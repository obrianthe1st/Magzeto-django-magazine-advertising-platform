from django.contrib import admin

from .models import (
    SearchAdClicks,
    SearchAdImpression,
    SponsoredAdClicks,
    SponsoredAdImpression,
)


# Register your models here.
class SearchAdClicksAdmin(admin.ModelAdmin):
    list_display = ('advertisement_name','cpc','clicks','time_stamp','searchad_id')
    list_filter = ('created',)
    date_hierarchy = 'created'

class SearchAdImpressionsAdmin(admin.ModelAdmin):
    list_display = ('advertisement_name','impressions','time_stamp','searchad_id')
    list_filter = ('created',)
    date_hierarchy = 'created'

class SponsoredAdClicksAdmin(admin.ModelAdmin):
    list_display = ('advertisement_name','cpc','clicks','time_stamp','sponsored_ad_id')
    list_filter = ('created',)
    date_hierarchy = 'created'

class SponsoredAdImpresionsAdmin(admin.ModelAdmin):
    list_display = ('advertisement_name','impressions','time_stamp','sponsored_ad_id')
    list_filter = ('created',)
    date_hierarchy = 'created'


admin.site.register(SearchAdClicks,SearchAdClicksAdmin)
admin.site.register(SearchAdImpression,SearchAdImpressionsAdmin)
admin.site.register(SponsoredAdClicks,SponsoredAdClicksAdmin)
admin.site.register(SponsoredAdImpression,SponsoredAdImpresionsAdmin)