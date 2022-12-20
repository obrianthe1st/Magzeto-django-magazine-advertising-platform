from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name =  forms.CharField(max_length=50,label='firstname')
    last_name = forms.CharField(max_length=50,label='lastname')
    phone_number = forms.CharField(max_length=50,label='phone number')


    def save(self,request):
        user = super(CustomSignupForm,self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.is_active=True
        user.save()
        return user



