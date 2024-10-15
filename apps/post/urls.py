from django.urls import path
from apps.post.views import *

app_name = "post"

urlpatterns = [
    path('post/crear', PostCrearView.as_view(), name='crearPost'),
    path('post/<int:pk>', PostMostrarView.as_view(), name='mostrarPost'),
]