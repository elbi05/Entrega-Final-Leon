from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    isbn=models.IntegerField()
    editorial=models.CharField(max_length=20)
    genero=models.CharField(max_length=30)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='books',null=True, blank=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Editorial: {self.editorial} - Genero: {self.genero} - Precio: {self.precio} - Imagen: {self.imagen}"