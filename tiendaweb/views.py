from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'prod.html')

def dproducto(request):
    return render(request, 'dpro.html')

def registro(request):
    return render(request, 'regi2.html')