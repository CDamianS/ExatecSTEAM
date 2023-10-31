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

science_cards = [
    {
        "title": "Áreas de oportunidad",
        "description": "Explora campos emergentes como la nanotecnología y sus aplicaciones.",
        "image": "img/science/áreas_de_oportunidad.jpg",
        "col": 4
    },
    {
        "title": "¿Cómo el arte soporta mi creatividad científica?",
        "description": "Descubre cómo el arte puede simplificar conceptos científicos y hacer que la ciencia sea más accesible.",
        "image": "img/science/como_el_arte_soporta_mi_creatividad_científica.jpeg",
        "col": 8
    },
    {
        "title": "¿Dónde puedo estudiar? Becas, Historias, Efemerides",
        "description": "Encuentra universidades destacadas en STEAM y conoce oportunidades de becas. Explora eventos históricos y efemérides científicas.",
        "image": "img/science/donde_puedo_estudiar.webp",
        "col": 8
    },
    {
        "title": "Infografía",
        "description": "Visualiza datos sobre la brecha de género en STEAM y la importancia de la diversidad de género.",
        "image": "img/science/infografia.webp",
        "col": 4
    },
    {
        "title": "¿Qué necesito para…?",
        "description": "Aprende qué se necesita para una carrera específica, como convertirte en astrónomo.",
        "image": "img/science/que_necesito_para.webp",
        "col": 4
    },
    {
        "title": "Héroes Reales: Historias Actuales",
        "description": "Conoce a científicos destacados, como la primatóloga Jane Goodall y la ingeniera química Frances Arnold.",
        "image": "img/science/heroes_reales.webp",
        "col": 8
    },
    {
        "title": "La mujer y la ingeniería",
        "description": "Descubre el impacto de las mujeres en STEAM y sus contribuciones, como el trabajo de Frances Arnold.",
        "image": "img/science/la_mujer_y_la_ingenieria.jpeg",
        "col": 8
    },
    {
        "title": "Bolsa de trabajo",
        "description": "Explora ofertas de empleo en STEAM, como posiciones en inteligencia artificial.",
        "image": "img/science/bolsa_de_trabajo.webp",
        "col": 4
    }
]
# Paginas STEAM
def science(request):
    context = {"seccion": "Science",
               "section_color": "#5371ff",
               "science_cards": science_cards,
               "impar": False}
    return render(request, "science.html", context)

def technology(request):
    return HttpResponse("Hello, world. You're at technology")

def engineering(request):
    return HttpResponse("Hello, world. You're at engineering")

def arts(request):
    return HttpResponse("Hello, world. You're at arts")

def math(request):
    return HttpResponse("Hello, world. You're at math")
