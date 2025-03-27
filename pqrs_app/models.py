from django.db import models

class Cliente(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    ]
    TIPO_PERMISOS = [
        ('A', 'Administrador'),
        ('C', 'Cliente'),
        ('G', 'Gestor')
    ]

    tipo_identificacion = models.CharField(max_length=2, choices=TIPO_IDENTIFICACION_CHOICES)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono_movil = models.CharField(max_length=15)
    permisos = models.CharField(max_length=2, choices=TIPO_PERMISOS,  default='C')

    def __str__(self):
        return self.nombre_completo

class PQRS(models.Model):
    TIPO_RADICADO_CHOICES = [
        ('P', 'Petición'),
        ('Q', 'Queja'),
        ('R', 'Reclamo'),
        ('S', 'Sugerencia'),
    ]

    numero_radicado = models.AutoField(primary_key=True)
    fecha_radicado = models.DateTimeField(auto_now_add=True)
    tipo_radicado = models.CharField(max_length=1, choices=TIPO_RADICADO_CHOICES)
    comentarios = models.TextField()
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pqrs')

    def __str__(self):
        return f"Radicado #{self.numero_radicado} - {self.tipo_radicado}"