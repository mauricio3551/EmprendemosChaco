from django.urls import path
from django.contrib.auth import views as auth
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.RegistroUsuario.as_view(), name = 'RegisterUsers'),
    path('login/', auth.LoginView.as_view(template_name='templates/usuarios/login.html'),name = 'login'),
    path('logout' , views.LogoutView.as_view() , name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    
]

