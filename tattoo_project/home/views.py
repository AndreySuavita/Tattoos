from django.views.generic.base import TemplateView
from .models import StudioImage

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['background_image'] = StudioImage.objects.filter(is_background=True).first()
        context['studio_images'] = StudioImage.objects.filter(is_background=False)
        return context
