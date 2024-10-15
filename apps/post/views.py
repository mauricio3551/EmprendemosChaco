from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from apps.post.forms import PostForm, CommentForm
from .models  import Post, Comment
from django.urls.base import reverse_lazy
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count


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