from django.apps import AppConfig


class CampaignConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label='campaign'
    name = "apps.ads.campaign"
