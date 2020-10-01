from django.shortcuts import render
from .models import Video


def home(request):
    video = Video.objects.all()
    return render(request, 'page/home.html',{'video':video})

def home2(request):
    return render(request, 'page/home2.html')

def blog(request):
    return render(request, 'page/blog.html')

def impuestos(request):
    return render(request, 'page/impuestos.html')

def finanzas(request):
    return render(request, 'page/finanzas.html')

def legal(request):
    return render(request, 'page/legal.html')

def opciones(request):
    return render(request, 'page/opciones.html')   

def terminos(request):
    return render(request, 'page/terminos.html')  

def politica(request):
    return render(request, 'page/politica.html')       