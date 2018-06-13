"""ge1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from . import views


""" ------------------------------------------------------------------------------ Imports ----- """
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, render
from front1.views import *
from tableroMando.views import *

from django.conf.urls import url

""" ------------------------------------------------------------------------------ Imports ----- """

urlpatterns = [
    
    # INICIO TABLERO DE MANDO
    path('inicio-TableroMando/', inicioTableroMando, name='inicio'),
    # PROGRAMACION
    # path('programacion/', programacion),

    # SEGUIMIENTO
    path('seguimiento/', seguimiento),

    # VER INDICADORES CREADOS

    # NUEVO INDICADOR
    # url(r'^nuevo_indicador/$', views.nuevo_indicador),

    # path('nuevo_indicador/', views.nuevo_indicador, name='nuevo_indicador'),
    # path('listar_indicadores/', listar_indicadores),
    # path('eliminar_indicador/', views.eliminar_indicador, name='eliminar_indicador'),
    # path('agregar_medicion/', views.agregar_medicion, name='agregar_medicion'),
    
    path('indicador/', ConfiguracionIndicador.as_view(), name='indicador'),

    path('programacion/', ProgramacionIndicador.as_view(), name='programacion'),


]   