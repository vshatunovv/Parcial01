from django.db import models

# Create your models here.

from django.db import models

class Flight(models.Model):
    tipo_vuelo = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=tipo_vuelo)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
