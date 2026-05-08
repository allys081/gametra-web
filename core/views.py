from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Juego


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
