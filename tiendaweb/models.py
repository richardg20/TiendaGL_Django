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

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tiendaweb_cliente'

class Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.CharField(max_length=7, default="0")
    cant_productos = models.CharField(max_length=7, default="0")
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    fecha = models.CharField(max_length=30, default="--/--/--_--:--:--")
    tipo_pago = models.CharField(max_length=30, default=" ")
    nro_orden = models.CharField(max_length=100, default="0")

    def __str__(self):
        return str(self.id) 
    
    class Meta:
        db_table = 'tiendaweb_boleta'

class Detalle_Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=500)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'tiendaweb_detalle_boleta'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password =  models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'tiendaweb_usuario'
