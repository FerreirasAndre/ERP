#Este arquivo contém as views do projeto ERP

from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("Bem vindo(a) ao sistema de Gestão UFF PLUS.")

def template_view(request):
    return render(request, 'template.html')