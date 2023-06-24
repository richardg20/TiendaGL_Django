from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=500, default="Descripcion")
    anno_lanzamiento = models.CharField(max_length=4, default="0")
    clasificacion  = models.CharField(max_length=2,default="")
    desarrollador = models.CharField(max_length=50,default="")
    genero = models.CharField(max_length=100,default="")
    id_video = models.CharField(max_length=30, default="")
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tiendaweb_producto'
