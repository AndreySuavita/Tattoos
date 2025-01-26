from django.contrib import admin
from .models import StudioImage, Background

class StudioAdmin(admin.ModelAdmin):
    model = StudioImage
    list_display = ['title', 'image','is_background']

class BackgroundAdmin(admin.ModelAdmin):
    model = Background
    list_display = ['title', 'image','is_background']

admin.site.register(StudioImage,StudioAdmin)
admin.site.register(Background,BackgroundAdmin)
