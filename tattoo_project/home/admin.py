from django.contrib import admin
from .models import StudioImage, Background, Logo

class StudioAdmin(admin.ModelAdmin):
    model = StudioImage
    list_display = ['title', 'image']

class BackgroundAdmin(admin.ModelAdmin):
    model = Background
    list_display = ['title', 'image','is_background']

class LogoAdmin(admin.ModelAdmin):
    model = Background
    list_display = ['title', 'image', 'is_the_logo']

admin.site.register(StudioImage,StudioAdmin)
admin.site.register(Background,BackgroundAdmin)
admin.site.register(Logo,LogoAdmin)
