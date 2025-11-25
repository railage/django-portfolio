from django.contrib import admin
from .models import Category, Photo, Service, ShootingType  # ДОБАВИЛИ ShootingType

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

# НОВЫЙ КЛАСС для админки
@admin.register(ShootingType)
class ShootingTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration']