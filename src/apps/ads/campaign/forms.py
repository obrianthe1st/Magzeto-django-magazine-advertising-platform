from django import forms

from .models import Campaign, SearchCampaign, SponsoredCampaign


class CampaignForm(forms.ModelForm):

    name = forms.CharField(max_length=150,label='Campaign Name')
    start_date = forms.DateField(label="start date")
    end_date = forms.DateField(label="end date")
    budget = forms.IntegerField(label="budget")

    class Meta:
        model = Campaign
        fields = ('name','start_date','end_date','budget',)

