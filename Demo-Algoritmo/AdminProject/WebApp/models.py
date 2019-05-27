from django.db import models

# Create your models here.
class Poblacion(models.Model):
    Departamento = models.TextField()
    Provincia = models.TextField()
    Distrito = models.TextField()
    Ciudad = models.TextField()
    Latitud = models.FloatField(null=True,blank=True, default=None)
    Longitud = models.FloatField(null=True,blank=True, default=None)

    
