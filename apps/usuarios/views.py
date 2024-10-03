from django.shortcuts import render
from .models import Item
from .forms import SearchForm
from datetime import date
from django.shortcuts import get_object_or_404

from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'Usuarios/profile_list.html', {'profiles': profiles})

def item_list(request):
    form = SearchForm(request.GET or None)
    items = Item.objects.all()

    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')
        author = form.cleaned_data.get('author')
        antiguedad = form.cleaned_data.get('antiguedad')
        order = form.cleaned_data.get('order')

        # Filtrar por búsqueda
        if search_term:
            items = items.filter(name__icontains=search_term)
        if category:
            items = items.filter(category=category)
        if author:
            items = items.filter(author__icontains=author)
        if antiguedad:
            fecha_limite = date.today().year - antiguedad
            items = items.filter(creation_date__year__lte=fecha_limite)

        # Ordenar
        if order:
            items = items.order_by(order)

    return render(request, 'item_list.html', {'form': form, 'items': items})

def home_view(request):
    return render(request, 'home.html')

def search_results(request):
    form = SearchForm(request.GET)
    items = Item.objects.none()  # Inicializa con un QuerySet vacío

    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')

        # Filtrar según la búsqueda
        if search_term:
            items = Item.objects.filter(name__icontains=search_term)
        if category:
            items = items.filter(category=category)

    return render(request, 'search_results.html', {'form': form, 'items': items})

def detalle_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'detalle_item.html', {'item': item})
