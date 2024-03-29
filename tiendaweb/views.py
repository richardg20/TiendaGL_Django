from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.views.decorators.http import require_POST
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import json
from .forms import MiFormulario
from django.contrib.auth import views as auth_views


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
     
        nombre_apellido = request.POST.get('firstName')
        rut = request.POST.get('rut')
        email = request.POST.get('email')
        direccion = request.POST.get('address')
        totalv = request.POST.get('totalv')
        cantidad_productos = request.POST.get('cantidad_productos')
        productos_list = json.loads(request.POST.get('productos_list'))


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


def admin(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'adminpro.html', context)
    

def aproducto(request):
    return render(request, 'addpro.html')



def add_producto(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        desc = request.POST.get('desc')
        anio = request.POST.get('anio')
        clas = request.POST.get('clas')
        dess = request.POST.get('dess')
        gen = request.POST.get('gen')
        idv = request.POST.get('idvid')
        imagen = request.FILES['imagen']

        producto = Producto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            anno_lanzamiento=anio,
            clasificacion=clas,
            desarrollador=dess,
            genero=gen,
            id_video=idv,
            imagen=imagen
        )
        producto.save()

        return redirect('administrador') 
    else:
        return HttpResponse('Error: Se requiere una solicitud POST')

    return render(request, 'addpro.html')


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'GET':

        producto.delete()
        return redirect('administrador')
    else:
        return HttpResponse('Error: Se requiere una solicitud GET')

def add_cliente(request):
    
    if request.method == 'POST':
       
        nombre_apellido = request.POST.get('firstName')
        rut = request.POST.get('rut')
        email = request.POST.get('email')
        direccion = request.POST.get('address')

        cliente, created = Cliente.objects.get_or_create(rut=rut)
        cliente.nombre = nombre_apellido
        cliente.email = email
        cliente.direccion = direccion
        cliente.save()

        return redirect('administrador') 
    else:
        return HttpResponse('Error: Se requiere una solicitud POST')

    return render(request, 'addcli.html')

def acliente(request):

    clientes=Cliente.objects.all()
    context = {"clientes":clientes}

    return render(request,'admincli.html',context)   

def addcliente(request):
    return render(request, 'addcli.html')


def eliminar_cliente(request, cliente_rut):
    cliente = get_object_or_404(Cliente, rut=cliente_rut)
    
    if request.method == 'GET':
        cliente.delete()
        return redirect('administrador')
    else:
        return HttpResponse('Error: Se requiere una solicitud GET')
    
def boletas(request):

    boletas = Boleta.objects.all()
    detalle_boletas = Detalle_Boleta.objects.all()
   
    context = {
        "boletas": boletas,
        "detalle_boletas": detalle_boletas
    }

    return render(request,'adminbol.html',context)



class LoginSystem(auth_views.LoginView):
    template_name = 'index.html' 

    def form_valid(self, form):

        if self.request.user.is_superuser:
            return super().form_valid(form)
        else:
            return HttpResponseRedirect('home')


def alterclientes(request, cliente_rut):

    cliente = Cliente.objects.get(rut = cliente_rut)
    context={"cliente":cliente}
    return render(request,'altercli.html',context)

def modclientes(request, cliente_rut):
 
    if request.method == 'POST':
       
        nombre_apellido = request.POST.get('firstName')
        email = request.POST.get('email')
        direccion = request.POST.get('address')

        cliente = Cliente.objects.get(rut = cliente_rut)
    
        cliente.nombre = nombre_apellido
        cliente.email = email
        cliente.direccion = direccion
        cliente.save()

        return redirect('acliente') 
    else:
        return HttpResponse('Error: Se requiere una solicitud POST')
 

