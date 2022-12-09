from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Author

#create a listdisplay, #this makes password field readonly

class AuthorAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','last_login','date_joined','is_active',)
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Author,AuthorAdmin)
