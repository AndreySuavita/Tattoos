# from django.views.generic.base import TemplateView
# from .models import Tattoo, TattooArtist

# class GalleryView(TemplateView):
#     template_name = 'tattoos/gallery_artist.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tattoos'] = Tattoo.objects.all()
#         context['artist'] = TattooArtist.objects.first()
#         return context

from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Tattoo, TattooArtist
from home.models import Background

class GalleryView(TemplateView):
    template_name = 'tattoos/gallery_artist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el artista usando el parámetro de la URL (id)
        artist = get_object_or_404(TattooArtist, pk=kwargs['pk'])  

        # Filtrar los tatuajes del artista
        context['artist'] = artist
        context['tattoos'] = Tattoo.objects.filter(artist=artist)

        # Poner fondos
        context['background_image'] = Background.objects.filter(is_background=True).first()
        return context

class ListArtist(TemplateView):
    template_name = 'tattoos/List_artists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = TattooArtist.objects.all()

        # poner fondos
        context['background_image'] = Background.objects.filter(is_background=True).first()
        return context