#Este arquivo contém as views do projeto ERP

from django.http import HttpResponse

#fazendo um teste de view
def teste_view(request):
    return HttpResponse("Hello, this is a test view.")

#fazendo uma view de index
def index_view(request):
    return HttpResponse("<h1>Welcome to the index page.</h>")