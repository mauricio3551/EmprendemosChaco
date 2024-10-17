from django.urls import path
from .views import *

app_name = "categoria"

urlpatterns = [
    path('categorias', categorias_view, name='categorias'),
]