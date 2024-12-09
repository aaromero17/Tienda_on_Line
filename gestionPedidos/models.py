from django.db import models

# Create your models here.

class Clientes(models.Model):
    
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)


class Articulos(models.Model):

    nombre=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedido(models.Model):

    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


