from django.urls import path
from apps.post.views import *

app_name = "post"

urlpatterns = [
    #post
    path('post/crear', PostCrearView.as_view(), name='crearPost'),
    path('post/<int:pk>', PostMostrarView.as_view(), name='mostrarPost'),

    #comentario
    path('post/<int:pk>/comentario', PostComentarioView.as_view(), name = 'nuevoComentario'),
    path('post/listar/comentario', postComentarios, name='listarComentarios')
]