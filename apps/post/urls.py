from django.urls import path
from apps.post.views import *

app_name = "posts"

urlpatterns = [
    path('post/crear', PostCrearView.as_view(), name='crearPost'),
]