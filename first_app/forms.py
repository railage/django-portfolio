from django import forms
from .models import Photo, Category
from django.core.exceptions import ValidationError


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'description', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Слишком короткое название (минимум 5 символов)')
        return title

