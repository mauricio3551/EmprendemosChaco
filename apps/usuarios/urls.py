from django.urls import path
from django.contrib.auth import views as auth
from . import views
from django.conf import settings


app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.RegistroUsuario.as_view(), name = 'RegisterUsers'),
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'login'),
    path('logout' , views.LogoutView.as_view() , name='logout'),
]

