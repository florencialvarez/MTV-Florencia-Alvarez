from django.db import models

# Create your models here.


class Familiar(models.Model):
    tipo_familiar = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()
