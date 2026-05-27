from django.shortcuts import render, redirect
from .models import Tickets, MetodoPago
from .forms import MetodoPagoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .forms import RegistroForm

# Create your views here.

# def index(request):
#     tickets = Tickets.objects.filter(tipo="cine")
#     return render(request, 'tickets/index.html', {'tickets': tickets})
@login_required
def cine(request):
    tickets = Tickets.objects.filter(tipo__icontains="cine")
    return render(request, 'tickets/cine.html', {'tickets': tickets})

@login_required
def tickets(request):
    todos_los_tickets = Tickets.objects.all() 
    return render(request, 'tickets/todos_los_tickets.html', {'tickets': todos_los_tickets})

@login_required
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

@login_required
def lista_metodos_pago(request):
    metodos = MetodoPago.objects.all()
    return render(request, 'tickets/lista_metodos.html', {'metodos': metodos})

@login_required
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

@login_required
def borrar_metodo(request, id):
    metodo = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        metodo.delete()
        return redirect('lista_metodos')
    return render(request, 'tickets/borrar_metodo.html', {'metodo': metodo})

#Registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cine')

    else:
        form = RegistroForm()

    return render(request, 'tickets/register.html', {
        'form': form,
        'hide_nav': True
    })


#Login de usuarios
def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = AuthenticationForm()

    return render(request, 'tickets/login.html', {
        'form': form,
        'hide_nav': True
    })


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')
