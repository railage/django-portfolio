from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Photo(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()  # ЭТО поле есть
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

class ShootingType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название съемки")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.CharField(max_length=100, verbose_name="Продолжительность")
    includes = models.TextField(verbose_name="Что входит")
    # ДОБАВЛЯЕМ ПОЛЕ ДЛЯ ФОТО
    image_url = models.URLField(verbose_name="Ссылка на фото", blank=True, null=True)

    def __str__(self):
        return self.name