from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'author', 'image']  # Incluyendo el nuevo campo 'image'

    # Opcional: Personaliza los widgets o las etiquetas
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Nombre del ítem'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Categoría'})
        self.fields['author'].widget.attrs.update({'placeholder': 'Autor'})


class SearchForm(forms.Form):
    search = forms.CharField(required=False, label='Buscar')
    category = forms.ChoiceField(choices=[
        ('', 'Todas las categorías'),
        ('Pintura', 'Pintura'),
        ('Comida', 'Comida'),
        ('Moda', 'Moda'),
        ('Muebles', 'Muebles'),
        ('Manualidades', 'Manualidades'),
        ('Musica', 'Musica'),
    ], required=False)
    author = forms.CharField(required=False, label='Autor')  # Campo para buscar por autor
    antiguedad = forms.IntegerField(required=False, label='Antigüedad (en años)')
    order = forms.ChoiceField(choices=[
        ('name', 'Ordenar por Nombre'),
        ('-name', 'Ordenar por Nombre (Z-A)'),
    ], required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'placeholder': 'Buscar ítem'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Categoría'})
        self.fields['author'].widget.attrs.update({'placeholder': 'Autor'})
        self.fields['antiguedad'].widget.attrs.update({'placeholder': 'Años'})



