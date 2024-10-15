
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormUsers
from .models import NewUser
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class RegistroUsuario(CreateView):
    model = NewUser
    template_name = 'usuarios/registro.html'
    form_class = FormUsers
    success_url = reverse_lazy('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect ('inicio')
