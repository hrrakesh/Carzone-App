from django.contrib import admin
from .models import Team

from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src= "{}" width="40" style="border-radius:25px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'



    list_display = ('id','thumbnail','first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('first_name','thumbnail',)
    search_fields = ('first_name','designation')
    list_filter = ('designation',)


# Register your models here.
admin.site.register(Team,TeamAdmin)