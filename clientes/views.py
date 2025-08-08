from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def lista_clientes(request):
    return HttpResponse("Lista de Clientes:")
def lista_clientes(request):
    return render(request, 'clientes/lista_clientes.html')