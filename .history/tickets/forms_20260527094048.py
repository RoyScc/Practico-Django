from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm
from .models import MetodoPago

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register_view(request):

    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            user = form.save()   # crea usuario
            login(request, user) # lo loguea
            return redirect("index")

    else:
        form = RegistroForm()

    return render(request, "tickets/register.html", {
        "form": form,
        "hide_nav": True
    })
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre', 'tipo', 'banco']