from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth
from . import views
from django.contrib.auth import views as auth_views


app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.RegistroUsuario.as_view(success_url = reverse_lazy('usuarios:registro_completo')), name = 'RegisterUsers'),
    path('registro/finalizado', views.RegistroUsuario.as_view(template_name = 'usuarios/registroCompleto.html'), name = 'registro_completo'),
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'login'),
    path('logout' , views.LogoutView.as_view() , name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    
]

