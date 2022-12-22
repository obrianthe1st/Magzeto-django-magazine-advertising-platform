from django.contrib import admin

from .models import Billing

# Register your models here.

class BillingAdmin(admin.ModelAdmin):
    list_display = ('card_holder','card_holder_name','country')
    list_filter = ('created',)
    date_hierarchy = 'created'

admin.site.register(Billing,BillingAdmin)


