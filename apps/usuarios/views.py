from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormUsers
from .models import NewUser


class RegistroUsuario(CreateView):
    model = NewUser
    template_name = 'usuarios/registro.html'
    form_class = FormUsers
    success_url = reverse_lazy('login')