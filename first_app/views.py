from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Photo, Category, Service, ShootingType
from .forms import ShootingTypeForm

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('/login/')

def is_manager(user):
    return user.is_staff


def home(request):
    photos = Photo.objects.all()
    shooting_types = ShootingType.objects.all()  # ДОБАВИЛИ ЭТУ СТРОКУ
    return render(request, 'portfolio/home.html', {
        'photos': photos,
        'shooting_types': shooting_types  # ДОБАВИЛИ ЭТУ СТРОКУ
    })

def photo_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    total_photos = Photo.objects.count()
    return render(request, 'portfolio/photo_detail.html', {
        'photo': photo,
        'total_photos': total_photos
    })


def services(request):
    services_list = Service.objects.all()
    shooting_types = ShootingType.objects.all()
    return render(request, 'portfolio/services.html', {
        'services': services_list,
        'shooting_types': shooting_types
    })


# ФУНКЦИЯ РЕГИСТРАЦИИ
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан! Теперь можно войти.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'portfolio/register.html', {'form': form})


# VIEW для добавления видов съемок (только для менеджеров)
@login_required
@user_passes_test(is_manager)
def add_shooting_type(request):
    if request.method == 'POST':
        form = ShootingTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ShootingTypeForm()

    return render(request, 'portfolio/add_shooting_type.html', {'form': form})