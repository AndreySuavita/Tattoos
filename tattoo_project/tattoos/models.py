from django.db import models

class TattooArtist(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Hacer el campo único
    photo = models.ImageField(upload_to='artists/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tattoo(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='tattoos/')
    artist = models.ForeignKey(
        TattooArtist,
        on_delete=models.CASCADE,
        related_name='tattoos',
        null=True,  # Permite que el valor sea NULL en la base de datos
        blank=True  # Permite que el formulario deje el campo vacío
    )

    def __str__(self):
        # Si no hay artista, muestra "Unknown Artist"
        artist_name = self.artist.name if self.artist else "Unknown Artist"
        return f"{self.title} by {artist_name}"

