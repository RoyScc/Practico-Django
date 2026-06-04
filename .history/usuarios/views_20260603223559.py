from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import UsuarioPersonalizadoForm

# Create your views here.

def registrarse(request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('cine')
    
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'registration/registrarse.html', {'form': form})
