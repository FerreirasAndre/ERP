from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#fazendo um teste de view
def teste_view(request):
    return HttpResponse("Hello, this is a test view.")


def template_view(request):
    return render(request,'template.html')

#Essa view renderiza um template HTML com o nome 'template.html'