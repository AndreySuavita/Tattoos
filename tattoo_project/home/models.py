from django.db import models

class StudioImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='studio/')
    is_background = models.BooleanField(default=False, help_text="Marcar como imagen de fondo")
    def __str__(self):
        return self.title or "Imagen de estudio sin título"
class Background(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='backgrounds/')
    is_background = models.BooleanField(default=False, help_text="Marcar como imagen de fondo")

    def __str__(self):
        return self.title or "Fondo sin Nombre"

