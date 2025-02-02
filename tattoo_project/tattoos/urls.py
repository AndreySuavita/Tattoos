from django.urls import path
from .views import Artist_GalleryView, ListArtist, Gallery
# "name" es utilzado para redireccionar los botones 
urlpatterns = [
    path('ListArtist/', ListArtist.as_view(), name='ListArtist'),
    path('Artist_Gallery/<int:pk>/', Artist_GalleryView.as_view(), name='Artist_Gallery'),
    path('gallery/', Gallery.as_view(), name='Gallery'),
]
