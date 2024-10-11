from django.urls import path
from . import views
from django.conf import settings


app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.RegistroUsuario.as_view(), name = 'RegisterUsers'),
]

