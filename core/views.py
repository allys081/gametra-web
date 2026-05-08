from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Juego
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def juegos(request):
    # Si el usuario inició sesión, ve todos los juegos
    if request.user.is_authenticated:
        juegos = Juego.objects.all()
    else:
        # Si es público, solo ve los que marcaste como 'es_publico'
        juegos = Juego.objects.filter(es_publico=True)

    return render(request, 'juegos.html', {'juegos': juegos})


@login_required  # Esto protege el área privada
def perfil(request):
    return render(request, 'perfil.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
