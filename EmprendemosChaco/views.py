from django.shortcuts import render
from apps.post.models import Post

def Inicio(request):
    recentPosts = Post.objects.order_by('-publish_date')[:3]
    return render(request, 'index.html', {'recentPosts': recentPosts})

def Login(request):
    return render(request, '')


