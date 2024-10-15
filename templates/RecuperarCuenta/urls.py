from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'recuperar'

urlpatterns = [
    path('reset/password_reset', auth_views.PasswordResetView.as_view(template_name='RecuperarCuenta/password_reset_form.html'), name = 'password_reset'),
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='RecuperarCuenta/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='RecuperarCuenta/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(template_name='RecuperarCuenta/password_reset_complete.html') , name = 'password_reset_complete'),
    
]