from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Profile
from .forms import SearchForm, ItemForm  # Asegúrate de importar 'ItemForm'
from datetime import date

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'Usuarios/profile_list.html', {'profiles': profiles})

def item_list(request):
    form = SearchForm(request.GET or None)
    items = Item.objects.all()

    if 'show_all' in request.GET:
        items = Item.objects.all()  # Mostrar todos los items si se hace clic en "Todo"
        print("Mostrando todos los ítems:", items)  # Imprime los ítems que se están mostrando

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

        print("Ítems después de aplicar filtros:", items)  # Imprime los ítems después de aplicar filtros

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

# Nueva vista para manejar la categoría
def categoria_view(request, categoria):
    items = Item.objects.filter(category=categoria)  # Filtra los ítems por categoría
    return render(request, 'categoria.html', {'items': items, 'categoria': categoria})

def pintura_1_view(request):
    return render(request, 'info_categ/pintura_1.html')  # Asegúrate de que la ruta sea correcta

def pintura_2_view(request):
    return render(request, 'info_categ/pintura_2.html')  # Asegúrate de que la ruta sea correcta


def item_form_view(request, item_id=None):
    if item_id:
        item = get_object_or_404(Item, id=item_id)  # Cargar el ítem existente
        form = ItemForm(request.POST or None, request.FILES or None, instance=item)  # Pasar el ítem existente al formulario
    else:
        form = ItemForm(request.POST or None, request.FILES or None)  # Crear un nuevo ítem

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('item_list')  # Redirigir a la lista de ítems después de guardar

    return render(request, 'item_form.html', {'form': form})  # Asegúrate de tener un template item_form.html




