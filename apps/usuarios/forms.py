from django import forms
from .models import Item

class SearchForm(forms.Form):
    search = forms.CharField(required=False, label='Buscar')
    category = forms.ChoiceField(choices=[
        ('', 'Todas las categorías'),
        ('cat1', 'Pintura'),
        ('cat2', 'Comida'),
        ('cat3', 'Moda'),
        ('cat4', 'Muebles'),
        ('cat5', 'Manualidades'),
        ('cat6', 'Musica'),
    ], required=False)
    author = forms.CharField(required=False, label='Autor')
    antiguedad = forms.IntegerField(required=False, label='Antigüedad (en años)')
    order = forms.ChoiceField(choices=[
        ('name', 'Ordenar por Nombre'),
        ('-name', 'Ordenar por Nombre (Z-A)'),
    ], required=False)
