from django.urls import path
from . import views # Import do arquivo que contém as URLs do projeto 
from django.http import HttpResponse

urlpatterns = [
    path('teste/', views.teste_view, name='teste_view'), # URL para a view de teste
    path('',views.template_view), # URL para a view de template
]