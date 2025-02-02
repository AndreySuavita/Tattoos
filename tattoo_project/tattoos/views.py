from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Tattoo, TattooArtist
from home.models import Background, Logo
import random

class Artist_GalleryView(TemplateView):
    template_name = 'tattoos/Gallery_artist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el artista usando el parámetro de la URL (id)
        artist = get_object_or_404(TattooArtist, pk=kwargs['pk'])  

        # Filtrar los tatuajes del artista
        context['artist'] = artist
        context['tattoos'] = Tattoo.objects.filter(artist=artist)
        # Poner fondo
        context['background_image'] = Background.objects.filter(is_background=True).first()
        # Poner Logo
        context['Logo'] = Logo.objects.filter(is_the_logo=True).first()
        return context

class ListArtist(TemplateView):
    template_name = 'tattoos/List_artists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # poner artista
        context['artists'] = TattooArtist.objects.all()
        # poner fondo
        context['background_image'] = Background.objects.filter(is_background=True).first()
        # Poner Logo
        context['Logo'] = Logo.objects.filter(is_the_logo=True).first()

        return context
    
class Gallery(TemplateView):
    template_name = 'tattoos/Gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Traer todos los tatuajes
        tattoos = list(Tattoo.objects.all())

        # Obtener el orden aleatorio y mantenerlo en la sesión
        session_key = 'tattoo_order'

        # Si no hay orden guardado en la sesión, generar uno nuevo
        if session_key not in self.request.session:
            random.shuffle(tattoos)
            # Guardar los IDs ordenados aleatoriamente
            self.request.session[session_key] = [tattoo.id for tattoo in tattoos]
            self.request.session.modified = True
        else:
            # Recuperar el orden de la sesión
            tattoo_order = self.request.session[session_key]
            tattoos = sorted(tattoos, key=lambda t: tattoo_order.index(t.id))

        context['tattoos'] = tattoos

        # Poner fondo
        context['background_image'] = Background.objects.filter(is_background=True).first()
        # Poner Logo
        context['Logo'] = Logo.objects.filter(is_the_logo=True).first()

        return context
