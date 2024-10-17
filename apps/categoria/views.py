from django.shortcuts import render
from .models import Categoria

def categorias_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})