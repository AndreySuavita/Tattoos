from django.views.generic.base import TemplateView
from .models import StudioImage, Logo

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['studio_images'] = StudioImage.objects.all()
        # poner logo
        context['Logo'] = Logo.objects.filter(is_the_logo=True).first()
        print(Logo.objects.filter(is_the_logo=True).first())
        return context
