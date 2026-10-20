from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):

    
    dados = {
        1: { "nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org/NASA/James Webb"

        },
        2: { "nome": "Galáxia NGC 1979",
        "legenda": "nasa.org / NASA / Hubble "

        }
    }

    return HttpResponse(render(request, 'galeria/index.html', {"cards": dados}))

def imagem(request):
    return HttpResponse(render(request, 'galeria/imagem.html'))