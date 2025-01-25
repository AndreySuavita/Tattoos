from django.contrib import admin
from .models import StudioImage

class TattooAdmin(admin.ModelAdmin):
    model = StudioImage
    list_display = ['title', 'image','is_background']

admin.site.register(StudioImage,TattooAdmin)
