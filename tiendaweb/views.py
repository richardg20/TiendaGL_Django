from django.shortcuts import render, get_object_or_404
from .models import Producto

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
