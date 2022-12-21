from django.db import models

from apps.authors.models import Author


# Create your models here.
class Billing(models.Model):

    COUNTRY_CHOICES = (("USA","USA"),
                       ("Jamaica","Jamaica"),
                       ("Canada","Canada"),
                       ("Bahamas","Bahamas"),
                       ("Cayman","Cayman"),
                       ("India","India"),)
    
    card_holder = models.ForeignKey(Author,on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=150)
    card_number = models.CharField(max_length=16)
    country = models.CharField(choices=COUNTRY_CHOICES,default="USA",max_length=20)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'billing'
        verbose_name_plural = 'billings'
        ordering = ['-created']

    def __str__(self):
        return self.card_holder_name



