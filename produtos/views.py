from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def lista_produtos(request):
    return HttpResponse("Lista de produtos")
def lista_produtos(request):
    return render(request, 'produtos/lista.html')