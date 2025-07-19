from django.shortcuts import render
from .models import Wallpaper, Audio

def home(request):
    return render(request, 'gallery/home.html')

def wallpaper(request):
    images = Wallpaper.objects.all()
    return render(request, 'gallery/wallpaper.html', {'images': images})

def audio(request):
    audios = Audio.objects.all()
    return render(request, 'gallery/audio.html', {'audios': audios})
