from django.db import models

class TicketPersonalizado(models.Model):
    ingresar_importe = models.FloatField()
    ingresar_empresa = models.CharField(max_length=150)
    ingresar_fecha = models.DateField()
    ingresar_hora = models.TimeField()
    descripcion = models.CharField(max_length=200)
    detalle_descripcion = models.TextField()
    descripcion_2 = models.CharField(max_length=200)
    detalle_descripcion_2 = models.TextField()
    descripcion_3 = models.CharField(max_length=200)
    detalle_descripcion_3 = models.TextField()
    descripcion_4 = models.CharField(max_length=200)
    detalle_descripcion_4 = models.TextField()
    def __str__(self):
        return self.ingresar_empresa
    