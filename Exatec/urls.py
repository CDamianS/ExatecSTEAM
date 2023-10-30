"""
URL configuration for Exatec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quienes-somos", views.quienes_somos, name="quienes_somos"),
    path("escuelas", views.escuelas, name="escuelas"),
    path("ninos-y-jovenes", views.ninos_y_jovenes, name="ninos_y_jovenes"),
    path("padres-de-familia", views.padres_de_familia, name="padres_de_familia"),
    path("eventos", views.noticias, name="eventos"),
    path("science/", views.science, name="science"),
    path("technology/", views.technology, name="technology"),
    path("engineering/", views.engineering, name="engineering"),
    path("arts/", views.arts, name="arts"),
    path("math/", views.math, name="math"),
    path("admin/", admin.site.urls),
]
