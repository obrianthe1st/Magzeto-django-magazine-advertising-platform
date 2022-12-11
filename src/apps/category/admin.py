from django.contrib import admin

from .models import Category, Tag

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated')
    list_filter = ('created',)
    prepopulated_fields = {"slug": ("name",)} 


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)