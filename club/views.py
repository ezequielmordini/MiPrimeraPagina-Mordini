from django.shortcuts import render, redirect
from .forms import JugadorForm, PartidoForm, NoticiaForm, BusquedaJugadorForm, SocioForm
from .models import Jugador
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print("Entro a la vista index")
    return render(request, 'club/index.html')


def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JugadorForm()    
    return render(request, 'club/agregar_jugador.html', {'form': form})

def agregar_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PartidoForm()
    return render(request, 'club/agregar_partido.html', {'form': form})

def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoticiaForm()
    return render(request, 'club/agregar_noticia.html', {'form': form})

def buscar_jugador(request):
    jugadores = None
    form = BusquedaJugadorForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    return render(request, 'club/buscar_jugador.html', {'form': form, 'jugadores': jugadores})

def registrar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'club/registrar_socio_exitoso.html')  
    else:
        form = SocioForm()
    return render(request, 'club/registrar_socio.html', {'form': form})
