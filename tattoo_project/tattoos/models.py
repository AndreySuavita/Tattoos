from django.db import models

class Tattoo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tattoos/')

    def __str__(self):
        return self.title

class TattooArtist(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artists/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
