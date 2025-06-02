#Este arquivo contém as views do projeto ERP

from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'FrontEnd/home.html')

def estoque_view(request):
    return render(request, 'FrontEnd/estoque.html')

def adicionar_estoque_view(request):
    return render(request, 'FrontEnd/adicionar-estoque.html')

def consultar_estoque_view(request):
    return render(request, 'FrontEnd/consultar-estoque.html')

def remover_estoque_view(request):
    return render(request, 'FrontEnd/remover-estoque.html')

def editar_estoque_view(request):
    return render(request, 'FrontEnd/editar-estoque.html')