from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

    # Técnicos disponibles
    TECNICOS = [
        ("Juan Pérez", "Juan Pérez"),
        ("María López", "María López"),
        ("Carlos Gómez", "Carlos Gómez"),
        ("Ana Torres", "Ana Torres"),
    ]

    asignado = forms.ChoiceField(
        choices=TECNICOS,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fecha_limite = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = Ticket
        fields = [
            'titulo',
            'descripcion',
            'solicitante',
            'telefono_contacto',
            'fecha_limite',
            'prioridad',
            'ubicacion',
            'asignado'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del ticket'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describa el problema'
            }),
            'solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del solicitante'
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono de contacto'
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ubicacion': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
