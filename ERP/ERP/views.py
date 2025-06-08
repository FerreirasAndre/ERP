#Este arquivo contém as views do projeto ERP

from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'FrontEnd/home.html')

def estoque_view(request):
    return render(request, 'FrontEnd/estoque.html')