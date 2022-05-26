from django.db import models

class Detalle(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DNI = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    Esta_Vivo = models.BooleanField(default=True)
    Observaciones = models.CharField(max_length=200, blank=True, null=True)