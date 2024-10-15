from django import forms
from .models import Post, Comment
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'category']
        labels = {'title': 'Ingrese un titulo', 'content': 'Informacion', 'thumbnail': 'imagen', 'category': 'categoria'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Agregar un comentario'}