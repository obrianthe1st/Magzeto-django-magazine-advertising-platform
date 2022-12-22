from django import forms

from apps.ads.advert.models import SearchAd, SponsoredAd

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

class CreateSearchAdForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    description = forms.CharField(max_length=500,widget=forms.Textarea())
    link = forms.URLField(max_length=150)

    class Meta:
        model = SearchAd
        fields = ("title","description","link",)

class CreateSponsoredAdForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    description = forms.CharField(max_length=500,widget=forms.Textarea())
    image = forms.ImageField()
    link = forms.URLField(max_length=150)

    class Meta:
        model = SponsoredAd
        fields = ("title","description","link","image")