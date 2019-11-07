from django.db import models

# Create your models here.
class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='perro/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return "Perro: {}".format(self.nombre)