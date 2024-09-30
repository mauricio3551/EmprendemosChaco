from django.shortcuts import render

from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'Usuarios/profile_list.html', {'profiles': profiles})