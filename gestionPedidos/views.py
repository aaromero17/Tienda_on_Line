from django.shortcuts import render
from django.http import HttpResponse

def busqueda_productos(request):

    return render(request,"busqueda_productos.html")


def buscar(request):
    mensaje=f"articulo buscado: {request.GET['prd']}"
    return HttpResponse(mensaje)