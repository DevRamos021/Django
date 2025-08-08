from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def lista_pedidos(request):
    return HttpResponse("Lista de pedidos:")
def lista_pedidos(request):
    return render(request, 'pedidos/lista_pedidos.html')