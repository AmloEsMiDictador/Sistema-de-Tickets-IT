from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login as auth_login,logout # Renombramos login para evitar conflicto

# Create your views here.
from .forms import TicketForm
from .models import Ticket, EstatusTicket, Usuario

# -- Login y Logout --
def login(request):
    if request.method == 'POST':

        numero_control = request.POST.get('numero_control')
        clave = request.POST.get('password')

        user = authenticate(request, numero_control=numero_control, password=clave)

        if user is not None:
            auth_login(request, user)
            return redirect(reverse('dashboard'))
        else:
            return render(request, 'login.html', {'error': 'Número de control o contraseña incorrectos.'})

    # si es GET
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# -- Plantilla --
def sideBar (request):
    return render(request, "sideBar.html")

# -- Vistas Principales --

@login_required
def tickets(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        prioridad = request.POST.get("prioridad")
        fecha_limite = request.POST.get("fecha_limite")
        ubicacion = request.POST.get("ubicacion")
        telefono_contacto = request.POST.get("telefono_contacto")

        estatus_inicial = EstatusTicket.objects.first()

        Ticket.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad,
            fecha_limite=fecha_limite if fecha_limite else None,
            ubicacion=ubicacion,
            telefono_contacto=telefono_contacto,
            solicitante=request.user,
            estatus=estatus_inicial,
        )
        return redirect("dashboard")
    return render(request, "tickets.html")

def kanban(request):
    nuevo = Ticket.objects.filter(estatus="Nuevo")
    enviado = Ticket.objects.filter(estatus="Enviado")  # <-- si existe
    en_progreso = Ticket.objects.filter(estatus="En progreso")
    finalizado = Ticket.objects.filter(estatus="Completado")
    context = {
        "nuevo": nuevo,
        "en_progreso": en_progreso,
        "finalizado": finalizado,
    }
    return render(request, "kanban.html", context)

def dashboard(request):
    return render(request, "dashboard.html")

def users(request):
    return render(request, "users.html")

def settings(request):
    return render(request, "settings.html")

def newTicket(request):
    return render(request, "newTicket.html")



#ROLES DE ACCESO ADMINISTRADOR
def rol_tecnico_o_admin(user):
    return user.groups.filter(name__in=["Tecnico", "Administrador"]).exists()

@user_passes_test(rol_tecnico_o_admin)
def vista_tecnico(request):
    return render(request, "tickets.html")

from .models import Ticket, TicketLog

def ticket_detalle(request, id):
    ticket = Ticket.objects.get(id=id)

    historial = TicketLog.objects.filter(ticket=ticket).order_by("-fecha")

    if request.method == "POST":
        comentario = request.POST.get("comentario")
        TicketLog.objects.create(
            ticket=ticket,
            accion="Comentario añadido",
            detalle=comentario
        )
        return redirect("ticket_detalle", id=id)

    return render(request, "tickets.html", {
        "ticket": ticket,
        "historial": historial
    })
