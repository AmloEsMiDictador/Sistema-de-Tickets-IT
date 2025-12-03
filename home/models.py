from django.db import models
from django.contrib.auth.models import AbstractUser

# =========================================================
# Custom User
# =========================================================
class Usuario(AbstractUser):
    numero_control = models.CharField(max_length=20, unique=True)
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)

    departamento = models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True, blank=True)
    puesto = models.ForeignKey('Puesto', on_delete=models.SET_NULL, null=True, blank=True)

    TIPO_CHOICES = [
        ('usuario', 'Usuario'),
        ('admin', 'Administrador'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='usuario')

    estatus = models.ForeignKey('EstatusUsuario', on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = "numero_control"
    REQUIRED_FIELDS = ["username"]  # Para que Django genere migraciones correctamente

    def __str__(self):
        return f"{self.numero_control} - {self.nombre} {self.apellidos}"

# =========================================================
# Departamento
# =========================================================
class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


# =========================================================
# Puesto
# =========================================================
class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='puestos')

    class Meta:
        unique_together = ('nombre', 'departamento')

    def __str__(self):
        return f"{self.nombre} - {self.departamento.nombre}"


# =========================================================
# Estatus de usuario
# =========================================================
class EstatusUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# =========================================================
# Estatus de ticket
# =========================================================
class EstatusTicket(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# =========================================================
# Ticket
# =========================================================
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# =========================================================
# Ticket (¡ESTE FALTABA!)
# =========================================================
# home/models.py

from django.db import models
class Ticket(models.Model):

    # Opciones de prioridad
    PRIORIDADES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    # Ubicaciones disponibles
    UBICACIONES = [
        ('Flute Automation', 'Flute Automation'),
        ('Flute Machining', 'Flute Machining'),
    ]

    # Estatus del ticket
    ESTATUS = [
        ('Nuevo', 'Nuevo'),
        ('En progreso', 'En progreso'),
        ('Completado', 'Completado'),
    ]

    # Asignados disponibles (nombres aleatorios)
    ASIGNADOS = [
        ('Juan Perez', 'Juan Perez'),
        ('Maria Lopez', 'Maria Lopez'),
        ('Carlos Diaz', 'Carlos Diaz'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    solicitante = models.CharField(max_length=100)   # quien crea el ticket

    asignado = models.CharField(
        max_length=100,
        choices=ASIGNADOS,
        blank=True,
        null=True
    )

    prioridad = models.IntegerField(choices=PRIORIDADES, default=2)

    telefono_contacto = models.CharField(max_length=30, blank=True)

    fecha_limite = models.DateField(null=True, blank=True)

    ubicacion = models.CharField(max_length=50, choices=UBICACIONES)

    estatus = models.CharField(
        max_length=20,
        choices=ESTATUS,
        default='Nuevo'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_prioridad_display()})"
    
class TicketLog(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="logs")
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log de Ticket #{self.ticket.id} - {self.fecha}"
