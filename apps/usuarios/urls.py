from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth
from . import views
from django.conf import settings


app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.RegistroUsuario.as_view(success_url = reverse_lazy('usuarios:registro_completo')), name = 'RegisterUsers'),
    path('registro/finalizado', views.RegistroUsuario.as_view(template_name = 'usuarios/registroCompleto.html'), name = 'registro_completo'),
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'login'),
    path('logout' , views.LogoutView.as_view() , name='logout'),
]

