from django.shortcuts import render
#from django.http import HttpResponse
from . import forms

def index(request):
    return render(request, "vendas/index.html")

#.................... CONTA ..................
def login(request):
    return render(request, "vendas/conta/login.html")

def cadastro(request):
    return render(request, "vendas/conta/cadastro.html")
#....................................................

#.................... NAVBAR LINKS ..................
def lojas(request):
    return render(request, "vendas/navbar/lojas.html")

def computadores(request):
    return render(request, "vendas/navbar/computadores.html")

def tablets(request):
    return render(request, "vendas/navbar/tablets.html")

def drones_camera(request):
    return render(request, "vendas/navbar/drones_camera.html")

def audio(request):
    return render(request, "vendas/navbar/audio.html")

def mobile(request):
    return render(request, "vendas/navbar/mobile.html")

def tv_home_theater(request):
    return render(request, "vendas/navbar/tv_home_theater.html")

def tec_vestivel(request):
    return render(request, "vendas/navbar/tec_vestivel.html")

def promocoes(request):
    return render(request, "vendas/navbar/promocoes.html")
#....................................................