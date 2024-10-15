from django.urls import path, reverse_lazy
from .views import CategoriaCrearView
from django.conf import settings
from django.conf.urls.static import static

app_name = "categoria"

urlpatterns = [
    # url para agregar categorias
    path('categoria/agregar', CategoriaCrearView.as_view(success_url = reverse_lazy('categoria:categoriaCreada')), name='crearCategoria'),
    path('categoria/creada/', CategoriaCrearView.as_view(template_name = 'categorias/categoriaCreada.html'), name='categoriaCreada'),
]