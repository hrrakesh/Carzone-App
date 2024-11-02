from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Car_at_top

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'model', 'color', 'year', 'features', 'condition', 'is_featured','created_at','for_rented')
    list_display_links = ('thumbnail', 'car_title')

    search_fields = ('car_title', 'engine')
    list_filter = ('is_featured',)

    list_editable = ('is_featured','for_rented')


class Car_at_top_Admin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;" />'.format(object.car_image_at_top.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'car_title', 'description')
    list_display_links = ('thumbnail', 'car_title')

    search_fields = ('car_title', 'id')
    
# Register Car with CarAdmin
admin.site.register(Car, CarAdmin)

# Register Car_at_top with default admin
admin.site.register(Car_at_top,Car_at_top_Admin)
