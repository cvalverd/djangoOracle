from django.db import models
from django.utils import timezone


class Productos(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')


    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.nombre
