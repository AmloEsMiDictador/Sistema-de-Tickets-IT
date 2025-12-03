import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from home.models import Ticket


def run():
    # Lista de nombres para asignado
    asignados = [
        "Carlos Mendez",
        "María Soto",
        "Juan Ramirez",
        "Laura Hernandez",
        "Pedro Martinez",
    ]

    ubicaciones = ["Flute Automation", "Flute Machining"]

    # Crear 10 tickets de prueba
    for i in range(10):
        Ticket.objects.create(
            titulo=f"Problema generado #{i+1}",
            descripcion="Descripción automática para pruebas.",
            asignado=asignados[i % len(asignados)],
            ubicacion=ubicaciones[i % len(ubicaciones)],
            estatus="Nuevo"  # siempre nuevo
        )

    print("Tickets creados exitosamente!")


if __name__ == "__main__":
    run()
