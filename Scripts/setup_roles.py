import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Crear grupos
roles = ["Administrador", "Tecnico", "Usuario"]

for role in roles:
    Group.objects.get_or_create(name=role)

print("Roles creados correctamente.")
