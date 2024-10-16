"""
URL configuration for EmprendemosChaco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
from .views import CustomPasswordResetView
from django.contrib.auth.views import PasswordResetDoneView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio, name='inicio'),
    path('logout' , LogoutView.as_view(next_page='inicio') , name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('usuarios/', include('apps.usuarios.urls')),
    path('', include('apps.post.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    

