from django.contrib import admin
from .models import Tattoo, TattooArtist

class TattooAdmin(admin.ModelAdmin):
    model = Tattoo
    list_display = ['artist','title', 'image']

class TattooArtistAdmin(admin.ModelAdmin):
    model = TattooArtist
    list_display = ['name','photo', 'bio']

admin.site.register(Tattoo, TattooAdmin)
admin.site.register(TattooArtist, TattooArtistAdmin)


#old
# admin.site.register(Tattoo)
# admin.site.register(TattooArtist)
