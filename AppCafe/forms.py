from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

# class ClienteFormulario(forms.Form):
#     nombre=forms.CharField(max_length=30)
#     email=forms.EmailField()

# class CuentaFormulario(forms.Form):
#     total=forms.IntegerField()
#     mesa=forms.IntegerField()

class LibroFormulario(forms.Form):
    titulo=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=30)
    isbn=forms.IntegerField()
    editorial=forms.CharField(max_length=20)
    genero=forms.CharField(max_length=30)
    precio=forms.IntegerField()
    imagen=forms.ImageField(label="Book",required=False)

class UserRegisterForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repite la contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields=['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password=None
    email=forms.EmailField(label="Ingrese su email")
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")

    class Meta:
        model=User
        fields=['email','last_name','first_name']
        help_texts={k:"" for k in fields}

class AvatarFormulario(UserChangeForm):
    password=None
    imagen = forms.ImageField(required=True)

    class Meta:
        model=User
        fields=['imagen']
    