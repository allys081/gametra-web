from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required  # solo usuarios logueados pueden entrar
def perfil(request):
    return render(request, 'perfil.html')


def juegos(request):
    return render(request, 'juegos.html')
