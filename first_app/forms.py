from django import forms
from .models import Photo, Category, ShootingType

# ИСПРАВЛЕННАЯ ФОРМА - убрали поле image
class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image_url', 'description', 'category']  # ЗАМЕНИЛИ image на image_url

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Слишком короткое название (минимум 5 символов)')
        return title

from django import forms
from .models import ShootingType

class ShootingTypeForm(forms.ModelForm):
    class Meta:
        model = ShootingType
        fields = ['name', 'description', 'price', 'duration', 'includes', 'image_url']  # ДОБАВИЛИ image_url
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Детская фотосессия'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Подробное описание съемки'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в рублях'
            }),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 2 часа'
            }),
            'includes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Что входит в стоимость (обработанные фото, фотоальбом и т.д.)'
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/photo.jpg'
            }),
        }
        labels = {
            'name': 'Название съемки',
            'description': 'Описание',
            'price': 'Цена (руб)',
            'duration': 'Продолжительность',
            'includes': 'Что входит',
            'image_url': 'Ссылка на фото',
        }