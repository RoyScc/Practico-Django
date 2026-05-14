from django.shortcuts import render, redirect
from .models import Tickets, MetodoPago
from .forms import MetodoPagoForm

# Create your views here.

# def index(request):
#     tickets = Tickets.objects.filter(tipo="cine")
#     return render(request, 'tickets/index.html', {'tickets': tickets})

def cine(request):
    tickets = Tickets.objects.filter(tipo__icontains="cine")
    return render(request, 'tickets/cine.html', {'tickets': tickets})

def tickets(request):
    todos_los_tickets = Tickets.objects.all() 
    return render(request, 'tickets/todos_los_tickets.html', {'tickets': todos_los_tickets})

def crear_metodo_pago(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_metodos')
    else:
        form = MetodoPagoForm()
    return render(request, 'tickets/crear_metodo_pago.html', {'form': form})

from django.shortcuts import get_object_or_404

def lista_metodos_pago(request):
    metodos = MetodoPago.objects.all()
    return render(request, 'tickets/lista_metodos.html', {'metodos': metodos})

def editar_metodo(request, id):
    metodo = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodo)
        if form.is_valid():
            form.save()
            return redirect('lista_metodos') 
    else:
        form = MetodoPagoForm(instance=metodo) 
    return render(request, 'tickets/crear_metodo_pago.html', {'form': form})

def borrar_metodo(request, id):
    metodo = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        metodo.delete()
        return redirect('lista_metodos')
    return render(request, 'tickets/borrar_metodo.html', {'metodo': metodo})
