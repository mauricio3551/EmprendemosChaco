from django import forms
from .models import Post
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'miniatura', 'categoria']
        labels = {'titulo': 'Ingrese un titulo'}