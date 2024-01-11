from django.db import models

class TicketPersonalizado(models.Model):
    ingresar_importe = models.FloatField(null=True,)
    ingresar_empresa = models.CharField(max_length=150, null=True)
    ingresar_fecha = models.DateField(null=True, default='2000-01-01')
    ingresar_hora = models.TimeField(null=True, default='00:00')
    descripcion = models.CharField(max_length=200, null=True)
    detalle_descripcion = models.TextField(null=True)
    descripcion_2 = models.CharField(max_length=200, null=True)
    detalle_descripcion_2 = models.TextField(null=True)
    descripcion_3 = models.CharField(max_length=200, null=True)
    detalle_descripcion_3 = models.TextField(null=True)
    descripcion_4 = models.CharField(max_length=200, null=True)
    detalle_descripcion_4 = models.TextField(null=True)

    def __str__(self):
        return self.ingresar_empresa

class TicketSameep(models.Model):
    nombre_apellido_cliente = models.CharField(max_length=250)
    cliente_suministro = models.TextField()
    ingresar_factura = models.IntegerField()
    ingresar_fecha = models.DateField()
    ingresar_hora = models.TimeField()
    paysen_ID = models.IntegerField()
    importe = models.FloatField()
    codigo_verificacion = models.IntegerField()

    def __str__(self):
        return self.nombre_apellido_cliente
    
class AbrirPromoEscolar(models.Model):
    nombre_apellido_tutor = models.CharField(max_length=250)
    monto_a_abonar = models.FloatField()
    nombre_apellido_alumno = models.CharField(max_length=250)
    curso = models.CharField(max_length=50)
    N_cuota = models.IntegerField()
    colegio = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre_apellido_alumno,self.nombre_apellido_tutor
    
class RegistartPagoNaranja(models.Model):
    DNI_Titular = models.IntegerField()
    Nombre_Titular = models.CharField(max_length=250)
    importe = models.FloatField()
    ingresar_fecha = models.DateField()
    ingresar_hora = models.TimeField()
    N_transaccion = models.FloatField()
    N_operacion = models.IntegerField()
    telefono_titular = models.BigIntegerField()
    #falta agregar colaborador y hacer una seccion de buscar pago
    def __str__(self):
        return self.Nombre_Titular

