from django.db import models

from ..authors.models import Author
from ..category.models import Category, Tag

# Create your models here.

class Article(models.Model):

   """
   A class for the article model
   """
   title = models.CharField(max_length=300)
   author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
   category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
   tag = models.ManyToManyField(Tag)
   slug = models.SlugField(max_length=300,unique=True)
   image = models.ImageField(upload_to='articles/', default='default/default.png')
   posts = models.TextField(max_length=4000)
   created = models.DateTimeField(auto_now_add=True,editable=False)
   updated = models.DateTimeField(auto_now=True)

   class Meta:
    verbose_name = 'article'
    verbose_name_plural = 'articles'

   def __str__(self):
    return self.title

#    def get_absolute_url(self):
#        return reverse("model_detail", args={self.pk})
   