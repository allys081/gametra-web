from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Juego, Reseña
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
            # EL MENSAJE VA AQUÍ:
            messages.success(
                request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def crear_juego(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        es_publico = request.POST.get('es_publico') == 'on'

        Juego.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            es_publico=es_publico,
            creado_por=request.user
        )
        # EL MENSAJE VA AQUÍ:
        messages.success(
            request, f'¡El juego "{titulo}" se ha publicado con éxito!')
        return redirect('juegos')

    return render(request, 'crear_juego.html')


@login_required
def dejar_resena(request, juego_id):
    if request.method == 'POST':
        juego = Juego.objects.get(id=juego_id)
        comentario = request.POST.get('comentario')
        # Guardamos la reseña vinculada al usuario actual
        Reseña.objects.create(
            juego=juego,
            usuario=request.user,
            comentario=comentario,
            calificacion=5  # O el valor que captures
        )
    return redirect('detalle_juego', juego_id=juego_id)


def detalle_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'detalle_juego.html', {'juego': juego})
