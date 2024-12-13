from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.form import FormularioContacto


def busqueda_productos(request):

    return render(request,"busqueda_productos.html")


def buscar(request):

    if request.GET['prd']:
       # mensaje=f"articulo buscado: {request.GET['prd']}"

       
       
       
       producto=request.GET['prd']
       articulos=Articulos.objects.filter(nombre__icontains=producto)
       return render(request,"resultado_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has introducido la busqueda"
    
    return HttpResponse(mensaje)


def contacto(request):

    if request.method=="POST":
        
        
        
         #return render(request,"gracias.html")

        #return render(request,"contacto.html")

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            inform=miFormulario.cleaned_data
            return render(request,"gracias.html")
    else:
       miFormulario=FormularioContacto()

    return render(request,"formulario_contacto.html",{"form":miFormulario})