from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField(max_length=7)
    descripcion = models.CharField(max_length=500, default="Descripcion")
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre
