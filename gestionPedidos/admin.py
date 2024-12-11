from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedido


class ClientesAdmin(admin.ModelAdmin):#Agrega mas campos de busqueda
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","telefono")#Agrega campos de busqueda

class ArticulosAdmin(admin.ModelAdmin):#Agregar filtros
    list_filter=("nombre","descripcion","precio")

class PedidosAdmin(admin.ModelAdmin):#Agregar filtros
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha" #Crea los filtros que estan encima de la lista "Migas de pan"


    

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedido,PedidosAdmin)





