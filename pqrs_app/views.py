from django.shortcuts import render, redirect
from .forms import ClienteForm

def home(request):
    return render(request, 'home.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario con la contraseña encriptada
            return redirect('home')  # Redirige a la página de inicio u otra página
    else:
        form = ClienteForm()
    return render(request, 'registrar.html', {'form': form})