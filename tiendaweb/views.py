from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import *
import json


# Create your views here.

def home(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'prod.html')
  

def dproductos(request, id):
    producto = get_object_or_404(Producto, id=id)
    print(producto)
    context = { "productos" : producto}
    return render(request, 'dpro.html', context)

def productos(request):
    return render(request, 'dpro.html')
  

def registro(request):
    return render(request, 'regi2.html')

def productos(request):
    productos = Producto.objects.all()
    print("Cantidad de productos:", len(productos))
    context = {"productos": productos}
    return render(request, 'prod.html', context)

def venta(request):
    return render(request, 'venta.html')


def confirmar_venta(request):

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_apellido = request.POST.get('firstName')
        rut = request.POST.get('rut')
        email = request.POST.get('email')
        direccion = request.POST.get('address')
        totalv = request.POST.get('totalv')
        cantidad_productos = request.POST.get('cantidad_productos')
        productos_list = json.loads(request.POST.get('productos_list'))


        # Imprimir los datos en la consola para verificar
        print('Nombre y Apellido:', nombre_apellido)
        print('Rut:', rut)
        print('Email:', email)
        print('Dirección:', direccion)

        cliente, created = Cliente.objects.get_or_create(rut=rut)
        cliente.nombre = nombre_apellido
        cliente.email = email
        cliente.direccion = direccion
        cliente.save()

        boleta = Boleta(total=totalv, cant_productos=cantidad_productos, rut_cliente=cliente)
        boleta.save()

        for producto in productos_list:
            detalle = Detalle_Boleta(producto=producto, id_boleta=boleta)
            detalle.save()

        return render(request, 'confirmacion.html')
    else:
        return HttpResponse('Error: Se requiere una solicitud POST')


    return render(request, 'confirmacion.html')