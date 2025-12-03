import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from home.models import Usuario

numero_control = "U001"
password = "1234"

if not Usuario.objects.filter(numero_control=numero_control).exists():
    user = Usuario.objects.create_user(
        numero_control=numero_control,
        password=password,
        username=numero_control  # requerido por REQUIRED_FIELDS
    )
    print("Usuario creado correctamente:", numero_control)
else:
    print("El usuario ya existe.")
