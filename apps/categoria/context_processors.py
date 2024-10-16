from .models import Categoria

def categoriasDisponibles(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}