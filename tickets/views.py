from django.shortcuts import render
from .models import Tickets

# Create your views here.

def index(request):
    tickets = Tickets.objects.filter(tipo="cine")
    return render(request, 'tickets/index.html', {'tickets': tickets})

def cine(request):
    tickets = Tickets.objects.filter(tipo="cine") | Tickets.objects.filter(tipo="Cine")
    return render(request, 'tickets/cine.html', {'tickets': tickets})

def carreras(request):
    tickets = Tickets.objects.filter(tipo="carreras") | Tickets.objects.filter(tipo="Carreras")
    return render(request, 'tickets/carreras.html', {'tickets': tickets})

def shows(request):
    tickets = Tickets.objects.filter(tipo="shows") | Tickets.objects.filter(tipo="Shows")
    return render(request, 'tickets/shows.html', {'tickets': tickets})