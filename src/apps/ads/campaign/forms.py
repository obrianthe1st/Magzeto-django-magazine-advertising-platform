from django import forms

from apps.ads.advert.models import SearchAd, SponsoredAd
from apps.ads.billing.models import Billing

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
    title = forms.CharField(label="title",max_length=150)
    description = forms.CharField(label="description",max_length=500,widget=forms.Textarea())
    link = forms.URLField(label="link",max_length=150)

    class Meta:
        model = SearchAd
        fields = ("title","description","link",)

class CreateSponsoredAdForm(forms.ModelForm):
    title = forms.CharField(label="title",max_length=150)
    description = forms.CharField(label="description",max_length=500,widget=forms.Textarea())
    image = forms.ImageField(label="image")
    link = forms.URLField(label="link",max_length=150)

    class Meta:
        model = SponsoredAd
        fields = ("title","description","link","image")

class BillingForm(forms.ModelForm):

    COUNTRY_CHOICES = (("USA","USA"),
                    ("Jamaica","Jamaica"),
                    ("Canada","Canada"),
                    ("Bahamas","Bahamas"),
                    ("Cayman","Cayman"),
                    ("India","India"),)

    country = forms.ChoiceField(label="country",choices=COUNTRY_CHOICES,widget=forms.Select(attrs={"class":"custom-select country-select"}))
    card_holder_name = forms.CharField(label="card holder name",max_length=150)
    card_number = forms.CharField(label="card number",max_length=16)
    month = forms.CharField(label="month",max_length=2)
    day = forms.CharField(label="day",max_length=2)
    cvc = forms.CharField(label="cvc",max_length=3)


    class Meta:
        model = Billing
        fields = ('country','card_holder_name','card_number','month',
        'day','cvc')


