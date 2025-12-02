from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as auth_login # Renombramos login para evitar conflicto

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect

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

def sideBar (request):
    return render(request, "sideBar.html")

def tickets(request):
    return render(request, "tickets.html")

def kanban(request):
    return render(request, "kanban.html")

def dashboard(request):
    return render(request, "dashboard.html")

def users(request):
    return render(request, "users.html")

def settings(request):
    return render(request, "settings.html")

def help(request):
    return render(request, "help.html")

#ROLES DE ACCESO ADMINISTRADOR
def rol_tecnico_o_admin(user):
    return user.groups.filter(name__in=["Tecnico", "Administrador"]).exists()

@user_passes_test(rol_tecnico_o_admin)
def vista_tecnico(request):
    return render(request, "tickets.html")
