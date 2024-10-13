from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from apps.post.forms import PostForm
from .models  import Categoria, Post, Comment
from django.urls.base import reverse_lazy
from django.conf import settings


class PostCrearView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/postForm.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    '''def form_valid(self, form):
        form.instance.usuario = self.request.user
        if form.instance.miniatura.name:
            ext = form.instance.miniatura.name.split(".")[-1]
            form.instance.miniatura.name = form.instance.titulo+'.'+ext
        return super().form_valid(form)'''