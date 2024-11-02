from django.contrib import admin
from .models import Contact,NonCarContact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','email','first_name','last_name','user_id','responded_view')
    list_display_links = ('id','email','first_name','last_name')
    search_fields = ('email','first_name','last_name')
    list_per_page = 25
    list_editable = ['responded_view']

class NonCarContactAdmin(admin.ModelAdmin):
    list_display = ('id','email','full_name','phone','responded_view')
    list_display_links = ('id','email','full_name')
    search_fields = ('email','full_name')
    list_per_page = 25
    list_editable = ['responded_view']

admin.site.register(Contact,ContactAdmin)

admin.site.register(NonCarContact,NonCarContactAdmin)
