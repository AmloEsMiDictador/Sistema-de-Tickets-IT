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
class Ticket(models.Model):
    PRIORIDADES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tickets_solicitados')
    asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')

    prioridad = models.IntegerField(choices=PRIORIDADES, default=2)
    fecha_limite = models.DateField(null=True, blank=True)

    ubicacion = models.CharField(max_length=200, blank=True)
    telefono_contacto = models.CharField(max_length=30, blank=True)

    estatus = models.ForeignKey(EstatusTicket, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_prioridad_display()})"
