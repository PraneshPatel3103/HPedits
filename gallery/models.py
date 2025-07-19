from django.db import models

class Wallpaper(models.Model):
    name = models.CharField(max_length=100)
    image_desktop = models.ImageField(upload_to='images/')
    image_mobile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Audio(models.Model):
    name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.name
