# Generated by Django 5.1.4 on 2024-12-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_alter_clientes_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='nombre',
            field=models.CharField(max_length=10, verbose_name='Nombre Articulo'),
        ),
    ]
