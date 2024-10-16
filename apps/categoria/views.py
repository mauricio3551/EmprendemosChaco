from django.shortcuts import render, get_object_or_404
from .forms import CategoriaForm
from .models import Categoria
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from apps.post.models import Post  # Importar el modelo de Post para listar los posts por categoría

class CategoriaCrearView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoriaForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  
        return context

# Vista para listar los posts por categoría
def listar_posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(category=categoria)
    return render(request, 'categoria/post_list_por_categoria.html', {'posts': posts, 'categoria': categoria})



