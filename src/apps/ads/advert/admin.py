from django.contrib import admin

from .models import SearchAd, SponsoredAd

# Register your models here.

class SearchAdAdmin(admin.ModelAdmin):
    list_display =  ('title','campaign_id','created','updated')
    list_filter = ('created',)
    date_hierarchy = 'created'

class SponsoredAdAdmin(admin.ModelAdmin):
    list_display =  ('title','campaign_id','created','updated')
    list_filter = ('created',)
    date_hierarchy = 'created'


admin.site.register(SearchAd,SearchAdAdmin)
admin.site.register(SponsoredAd,SponsoredAdAdmin)