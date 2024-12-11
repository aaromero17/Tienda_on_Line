from django.db import models

# Create your models here.

class Clientes(models.Model):
    
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)#el argumento hace que el campo sea opcional
    telefono=models.CharField(max_length=7,verbose_name="Telefono Cliente")# "Telefono cliente" es un alias

    def __str__(self):
        return self.nombre


class Articulos(models.Model):

    nombre=models.CharField(max_length=10,verbose_name="Nombre Articulo")
    descripcion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}, descripcion: {self.descripcion}, precio: {self.precio}"

class Pedido(models.Model):

    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return f"Numero: {self.numero}, Fecha: {self.fecha}, Entrega: {self.entregado}"


