from django.shortcuts import render
from .models import Photo, Category, Service


def home(request):
    photos = Photo.objects.all()
    return render(request, 'portfolio/home.html', {'photos': photos})


def photo_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    total_photos = Photo.objects.count()

    return render(request, 'portfolio/photo_detail.html', {
        'photo': photo,
        'total_photos': total_photos
    })


def services(request):
    services_list = Service.objects.all()
    return render(request, 'portfolio/services.html', {'services': services_list})

