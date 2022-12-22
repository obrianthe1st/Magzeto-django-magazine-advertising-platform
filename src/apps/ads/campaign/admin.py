from django.contrib import admin

from .models import SearchCampaign, SponsoredCampaign


# Register your models here.
class SearchCampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_manager','name','campaign_type','active','start_date','end_date','budget')
    list_filter = ('created',)
    date_hierarchy = 'created'

class SponsoredCampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_manager','name','campaign_type','active','start_date','end_date','budget')
    list_filter = ('created',)
    date_hierarchy = 'created'

admin.site.register(SearchCampaign,SearchCampaignAdmin)
admin.site.register(SponsoredCampaign,SponsoredCampaignAdmin)

