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