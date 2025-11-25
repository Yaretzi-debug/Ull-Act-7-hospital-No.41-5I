from django.db import models

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    tipo_sangre = models.CharField(max_length=10)
    fecha_registro = models.DateField()

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    num_licencia = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

class CitaMedica(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=50)
    observaciones = models.TextField()

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tratamiento_recomendado = models.TextField()
    nivel_gravedad = models.CharField(max_length=50)
    fecha_registro = models.DateField()

class FacturaHospital(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
