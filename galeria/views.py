from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(render(request, 'galeria/index.html'))

def imagem(request):
    return HttpResponse(render(request, 'galeria/imagem.html'))