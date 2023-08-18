from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html


class AdvertisementAdmin(admin.ModelAdmin):

   def image_tag(self, obj):
      return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

   list_display = ['id', 'title', 'description', 'created_date', 'updated_date', 'auction', 'image_tag']
   list_filter = ['created_at', 'auction']

admin.site.register(Advertisement, AdvertisementAdmin)



# Register your models here.
