from django.views.generic.base import TemplateView
from .models import Tattoo, TattooArtist

class GalleryView(TemplateView):
    template_name = 'tattoos/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tattoos'] = Tattoo.objects.all()
        context['artist'] = TattooArtist.objects.first()
        return context
