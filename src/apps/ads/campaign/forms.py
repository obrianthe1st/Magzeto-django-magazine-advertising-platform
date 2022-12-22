from django import forms

from .models import Campaign, SearchCampaign, SponsoredCampaign


class SearchCampaignForm(forms.ModelForm):

    name = forms.CharField(max_length=150,label='Campaign Name')
    start_date = forms.DateField(label="start date",widget=forms.DateInput(attrs=dict(type='date')))
    end_date = forms.DateField(label="end date",widget=forms.DateInput(attrs=dict(type='date')))
    budget = forms.IntegerField(label="budget")

    class Meta:
        model = SearchCampaign
        fields = ('name','start_date','end_date','budget',)


class SponsoredCampaignForm(forms.ModelForm):

    name = forms.CharField(max_length=150,label='Campaign Name')
    start_date = forms.DateField(label="start date",widget=forms.DateInput(attrs=dict(type='date')))
    end_date = forms.DateField(label="end date",widget=forms.DateInput(attrs=dict(type='date')))
    budget = forms.IntegerField(label="budget")

    class Meta:
        model = SponsoredCampaign
        fields = ('name','start_date','end_date','budget',)
