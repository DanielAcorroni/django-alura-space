from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):

  fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

  return render(request, 'galeria/index.html', { 'cards': fotografias })

def imagem(request, foto_id):

  fotografia = get_object_or_404(Fotografia, pk=foto_id)

  return render(request, 'galeria/imagem.html', { 'fotografia': fotografia })

def buscar(request):
  fotografias = False

  if "buscar" in request.GET:
    nome_busca = request.GET['buscar']
    if nome_busca:
      fotografias = Fotografia.objects.order_by(
        '-data_fotografia'
      ).filter(publicada=True, nome__icontains=nome_busca)

  return render(request, 'galeria/buscar.html', { 'cards': fotografias })