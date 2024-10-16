from django.urls import path, reverse_lazy
from .views import CategoriaCrearView, listar_posts_por_categoria  # Importa la vista para listar los posts por categoría
from django.conf import settings
from django.conf.urls.static import static

app_name = "categoria"

urlpatterns = [
    # URL para agregar categorías
    path('categoria/agregar', CategoriaCrearView.as_view(success_url=reverse_lazy('categoria:categoriaCreada')), name='crearCategoria'),
    path('categoria/creada/', CategoriaCrearView.as_view(template_name='categorias/categoriaCreada.html'), name='categoriaCreada'),

    # URL para listar los posts por categoría
    path('categoria/<int:categoria_id>/posts/', listar_posts_por_categoria, name='posts_por_categoria'),
]