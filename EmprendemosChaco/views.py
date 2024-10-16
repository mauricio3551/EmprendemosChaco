from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

def Inicio(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, '')

def about(request):
    return render(request, 'about.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')