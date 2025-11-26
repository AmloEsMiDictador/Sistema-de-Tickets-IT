from django.shortcuts import render

# Create your views here.
def login (request):
    return render(request, "login.html")

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