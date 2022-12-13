from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    """
    A class for category models
    """
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('category_view',args=[self.slug])

class Tag(models.Model):
    """
    A class for tag models
    """
    name = models.CharField(max_length=50,unique=True);
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(max_length=50,unique=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    
    def __str__(self):
        return self.name    
