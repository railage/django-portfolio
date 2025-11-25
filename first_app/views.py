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


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# ДОБАВЬ ЭТУ ФУНКЦИЮ В views.py
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Проверяем что пароли совпадают
        if password != password_confirm:
            messages.error(request, 'Пароли не совпадают!')
            return render(request, 'portfolio/register.html')

        # Проверяем что пользователь не существует
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует!')
            return render(request, 'portfolio/register.html')

        # Создаем пользователя
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Регистрация успешна! Теперь вы можете войти.')
        return redirect('home')

    return render(request, 'portfolio/register.html')