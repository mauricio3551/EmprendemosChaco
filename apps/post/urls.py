from django.urls import path, reverse_lazy
from apps.post.views import *

app_name = "post"

urlpatterns = [
    #post
    path('post/crear', PostCrearView.as_view(success_url = reverse_lazy('post:postCreado')), name='crearPost'),
    path('post/creado', PostCrearView.as_view(template_name = 'post/postCreationSuccess.html'), name = 'postCreado'),
    path('post/<int:pk>', PostMostrarView.as_view(), name='mostrarPost'),

    #comentario
    path('post/<int:pk>/comentario', PostComentarioView.as_view(), name = 'nuevoComentario'),
    path('post/listar/comentario', postComentarios, name='listarComentarios')
]