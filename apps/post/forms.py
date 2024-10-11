from django import forms
from .models import Post
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'category']
        labels = {'title': 'Ingrese un titulo'}