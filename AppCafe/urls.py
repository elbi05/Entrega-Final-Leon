from django.contrib import admin
from django.urls import path, include
from AppCafe.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',HomeListView.as_view(),name="Home"),
    path('inicio/', inicio, name="Inicio"),
    path('buscar/',buscar,name="Buscar"),
    path('busquedaLibro/',busquedaLibro, name="BusquedaLibro"),
    path('libro/lista',LibroListView.as_view(),name="ListaLibros"),
    path('libro/nuevo',LibroCreateView.as_view(),name="NuevoLibro"),
    path('libro/<pk>',LibroDetailView.as_view(),name="DetalleLibro"),
    path('libro/<pk>/editar',LibroUpdateView.as_view(),name="EditarLibro"),
    path('libro/<pk>/borrar',LibroDeleteView.as_view(),name="BorrarLibro"),
    path('login',login_request, name="Login"),
    path('register',register,name="Register"),
    path('logout',logout_request,name='Logout'),
    path('editarPerfil',editarPerfil,name="EditarPerfil"),
    path('cambiarContra',CambiarContra.as_view(),name="CambiarContra"),
    path('libro/',libro,name="Libro"),
    path('agregarAvatar', agregarAvatar, name="AgregarAvatar"),
    path('menuAdmin',menuAdmin,name="MenuAdmin")
]