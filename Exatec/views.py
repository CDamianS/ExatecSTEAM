from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Homepage
def index(request):
    return render(request, "homepage.html")


# Paginas navbar
def quienes_somos(request):
    return render(request, "quienes-somos.html")

def escuelas(request):
    return render(request, "escuelas.html")

def ninos_y_jovenes(request):
    return render(request, "ninos-y-jovenes.html")

def padres_de_familia(request):
    return render(request, "padres-de-familia.html")

def noticias(request):
    return render(request, "noticias.html")

def contacto(request):
    return render(request, "contacto.html")


# Paginas STEAM
def science(request):
    return HttpResponse("Hello, world. You're at science")

def technology(request):
    return HttpResponse("Hello, world. You're at technology")

def engineering(request):
    return HttpResponse("Hello, world. You're at engineering")

def arts(request):
    return HttpResponse("Hello, world. You're at arts")

def mathematics(request):
    return HttpResponse("Hello, world. You're at mathematics")
