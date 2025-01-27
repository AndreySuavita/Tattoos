from django.urls import path
from .views import GalleryView, ListArtist
# "name" es utilzado para redireccionar los botones 
urlpatterns = [
    path('gallery/<int:pk>/', GalleryView.as_view(), name='tattoos'),
    path('ListArtist/', ListArtist.as_view(), name='ListArtist'),
]
