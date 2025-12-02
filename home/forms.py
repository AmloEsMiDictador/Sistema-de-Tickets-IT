from django import forms
from .models import Ticket, Usuario

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "titulo",
            "descripcion",
            "prioridad",
            "fecha_limite",
            "ubicacion",
            "telefono_contacto",
            "solicitante",
            "asignado",
            "estatus",
        ]

        widgets = {
            "fecha_limite": forms.DateInput(attrs={"type": "date"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }
