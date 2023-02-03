from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages


def index(request):

    if not request.user.is_authenticated:
        messages.error(request, "Faça o login para poder vizualizar as fotos")
        return redirect("login")

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(
        publicada=True
    )

    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):

    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):

    if not request.user.is_authenticated:
        messages.error(request, "Faça o login para poder vizualizar as fotos")
        return redirect("login")

    fotografias = False

    if "buscar" in request.GET:
        nome_busca = request.GET["buscar"]
        if nome_busca:
            fotografias = Fotografia.objects.order_by(
                "-data_fotografia"
            ).filter(publicada=True, nome__icontains=nome_busca)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
