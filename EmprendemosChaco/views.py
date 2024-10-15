from django.shortcuts import render
from apps.post.models import Post
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

def Inicio(request):
    recentPosts = Post.objects.order_by('-publish_date')[:3]
    olderPost = Post.objects.order_by('-publish_date')[3:7]
    return render(request, 'index.html', {'recentPosts': recentPosts, 'olderPost':olderPost})

def Login(request):
    return render(request, '')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'Usuarios/password_reset.html'
    email_template_name = 'Usuarios/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')