from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from apps.post.forms import PostForm, CommentForm, EditPostForm
from .models  import Post, Comment
from django.urls.base import reverse_lazy
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Q
from apps.categoria.models import Categoria
from apps.usuarios.models import NewUser


class PostCrearView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/postForm.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.thumbnail.name:
            ext = form.instance.thumbnail.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title+'.'+ext
        return super().form_valid(form)
    
class PostMostrarView(DetailView):
    model = Post
    template_name = 'post/postShow.html'

    def getContextData(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostListView(ListView):
    model = Post
    ordering = ['-publish_date']
    template_name = 'post/postList.html'
    context_object_name = 'posts'

class PostEditarView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'post/postEdit.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def get_success_url(self):
        return reverse('post:mostrarPost', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user

        post = self.get_object()

        if not self.request.FILES.get('thumbnail'):
            form.instance.thumbnail = post.thumbnail

        else:
            if form.instance.thumbnail.name:
                ext = form.instance.thumbnail.name.split(".")[-1]
                form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user or self.request.user.is_superuser

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('inicio')

#--------------------COMENTARIOS-----------------------

class PostComentarioView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/postCommentForm.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        new = form.save(commit = False)
        new.post_id = self.kwargs['pk']
        new.user = self.request.user
        new.save()

        return HttpResponseRedirect(reverse('post:mostrarPost', args = [str(new.post_id)]))

def postComentarios(request):
    opcion = request.GET.get('select')
    posts = Post.objects.annotate(num_comments=Count('commentsPost')).order_by('-num_comments')

    return render(request,'post/postList.html', {'posts':posts})

#--------------------CATEGORIA-----------------------

class PostByCategoryView(ListView):
    model = Post
    template_name = 'categorias/categoriaFilter.html'
    context_object_name = 'postByCategory'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Post.objects.filter(category_id=category_id)

#--------------------BUSCADOR-----------------------

def search(request):
    return render(request, 'search.html')

def postSearchView(request):
    queryset = request.GET.get("buscar")

    resultado = {}
    categorias = Categoria.objects.all()
    resultado['categorias'] = categorias

    if queryset:
        user = NewUser.objects.filter(username = queryset)
        resultado['posts'] = Post.objects.filter(Q(title__icontains = queryset) | Q(user__in = user)).distinct()

    return render(request, 'busqueda/search.html', resultado)