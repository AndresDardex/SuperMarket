from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class Cliente(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
        ('Tarjeta de Identidad', 'Tarjeta de Identidad'),
        ('Cédula de Extranjería', 'Cédula de Extranjería'),
        ('Pasaporte', 'Pasaporte'),
    ]

    TIPO_PERMISOS_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Cliente', 'Cliente'),
        ('Gestor', 'Gestor'),
    ]

    VALIDACION_CHOICES = [
        ('Sí', 'Sí'),
        ('No', 'No'),
    ]

    tipo_identificacion = models.CharField(max_length=50, choices=TIPO_IDENTIFICACION_CHOICES)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono_movil = models.CharField(max_length=15)
    tipo = models.CharField(max_length=50, choices=TIPO_PERMISOS_CHOICES, default='Cliente')
    validacion = models.CharField(max_length=3, choices=VALIDACION_CHOICES, default='No')
    password = models.CharField(max_length=128, null=True, blank=True)  # Campo para almacenar contraseñas encriptadas

    def clean(self):
        # Validaciones adicionales si es necesario
        pass

    def save(self, *args, **kwargs):
        # Encripta la contraseña antes de guardar el modelo
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Verifica si la contraseña ingresada coincide con la almacenada
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.nombre_completo

class PQRS(models.Model):
    TIPO_RADICADO_CHOICES = [
        ('Petición', 'Petición'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia'),
    ]

    numero_radicado = models.AutoField(primary_key=True)
    fecha_radicado = models.DateTimeField(auto_now_add=True)
    tipo_radicado = models.CharField(max_length=25, choices=TIPO_RADICADO_CHOICES)
    comentarios = models.TextField()
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pqrs')

    def __str__(self):
        return f"Radicado #{self.numero_radicado} - {self.tipo_radicado}"