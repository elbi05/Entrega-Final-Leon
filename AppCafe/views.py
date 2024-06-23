from django.shortcuts import render,redirect
from AppCafe.models import *
from AppCafe.forms import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin


def home(req):
    return render(req, "AppCafe/home.html")

@login_required
def inicio(req):
    avatares=Avatar.objects.filter(user=req.user.id)
    return render(req, "AppCafe/inicio.html",{"url":avatares[0].imagen.url})

def buscar(req):
    return render(req,"AppCafe/buscar.html")

@login_required
def busquedaLibro(req):
    return render(req,"AppCafe/busquedaLibro.html")

@login_required
def buscar(req):
    if req.GET["libro"]:
        titulo=req.GET["libro"]
        libro=Libro.objects.filter(titulo__icontains=titulo)
        return render(req,"AppCafe/resultadosBusqueda.html",{"Libro":libro})
    else:
        respuesta="No enviaste datos"
    return render(req,"AppCafe/inicio.html",{"respuesta":respuesta})

def login_request(req):
    if req.method=="POST":
        form = AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']
            user = authenticate(username=usuario,password=contra)
            if user is not None:
                login(req,user)
                return render(req,"AppCafe/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(req,"AppCafe/inicio.html", {"mensaje":"Error, datos incorrectos!!!"})
        else:
            return render(req, "AppCafe/inicio.html", {"mensaje":"Error, formulario erroneo!!!"})
    form = AuthenticationForm()
    return render(req,"AppCafe/login.html",{'form':form})

def logout_request(req):
    logout(req)
    return redirect('Inicio')
    

def register(req):
    if req.method=='POST':
        form=UserRegisterForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(req,"AppCafe/inicio.html",{"mensaje":"Usuario creado"})
    else:
        form=UserRegisterForm()
    return render(req,"AppCafe/registro.html",{"form":form})

@login_required
def editarPerfil(req):
    usuario=req.user
    if req.method=='POST':
        miFormulario=UserEditForm(req.POST,req.FILES, instance=req.user)
        if miFormulario.is_valid():             
            miFormulario.save()
            return render(req,"AppCafe/inicio.html")
    else:
        miFormulario=UserEditForm(instance=req.user)
    return render(req,"AppCafe/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})

def libro(req):
    if req.method=='POST':
        miFormulario=LibroFormulario(req.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            libro=Libro(titulo=informacion['titulo'],autor=informacion['autor'],isbn=informacion['isbn'],editorial=informacion['editorial'],
                        genero=informacion['genero'],precio=informacion['precio'],imagen=informacion['imagen'])
            libro.save()
            return render(req,"AppCafe/inicio.html")
    else:
        miFormulario=LibroFormulario()
    return render(req,"AppCafe/libro.html",{"miFormulario":miFormulario})

@login_required
def agregarAvatar(req):
      usuario=req.user
      if req.method == 'POST':
            miFormulario = AvatarFormulario(req.POST,req.FILES, instance=req.user)
            if miFormulario.is_valid():              
                  avatar = Avatar (user=usuario, imagen=miFormulario.cleaned_data['imagen'])       
                  avatar.save()
                  return render(req,"AppCafe/inicio.html")
      else: 
            miFormulario= AvatarFormulario(instance=req.user)
      return render(req, "AppCafe/agregarAvatar.html", {"miFormulario":miFormulario})

@login_required
def menuAdmin(req):
    return render(req, "AppCafe/menuAdmin.html")



class LibroListView(ListView):
    model = Libro
    context_object_name="libros"
    template_name="AppCafe/libro_lista.html"

class LibroDetailView(DetailView):
    model = Libro
    template_name="AppCafe/libro_detalle.html"

class LibroCreateView(CreateView,LoginRequiredMixin):
    model = Libro
    template_name = "AppCafe/libro_crear.html"
    success_url= reverse_lazy('ListaLibros')
    fields=['titulo','autor','isbn','editorial','genero','precio','imagen']

class LibroUpdateView(UpdateView,LoginRequiredMixin):
    model = Libro
    template_name = "AppCafe/libro_editar.html"
    success_url=reverse_lazy('ListaLibros')
    fields=['titulo','autor','isbn','editorial','genero','precio','imagen']

class LibroDeleteView(DeleteView,LoginRequiredMixin):
    model = Libro
    template_name="AppCafe/libro_borrar.html"
    success_url=reverse_lazy('ListaLibros')

class CambiarContra(LoginRequiredMixin,PasswordChangeView):
    template_name='AppCafe/cambiarContra.html'
    success_url=reverse_lazy('EditarPerfil')

class HomeListView(ListView):
    model = Libro
    context_object_name="libros"
    template_name="AppCafe/home.html"




