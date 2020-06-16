from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListadoUsuario,RegistrarUsuario,inicioListadoUsuario
urlpatterns = [
    path('inicio_usuarios',login_required(inicioListadoUsuario.as_view()),name='inicio_usuarios'),


    path('listado_usuarios/',login_required(ListadoUsuario.as_view()),name='listado_usuarios'),
    path('registrar_usuario/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario')

]
