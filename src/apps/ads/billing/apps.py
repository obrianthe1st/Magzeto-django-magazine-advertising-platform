from django.apps import AppConfig


class BillingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = 'billing'  
    name = "apps.ads.billing"
