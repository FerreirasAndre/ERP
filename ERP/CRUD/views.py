from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .forms import CreateDataForm
from .models import Asset
from .serializers import AssetSerializer

import json


class AssetViewSet(viewsets.ModelViewSet):
	queryset = Asset.objects.all()
	serializer_class = AssetSerializer
	model = Asset
	tamplet_name = 'CRUD/asset_list.html'
	context_object_name = 'assets'

@api_view(['GET'])
def CRUD_retrieve(request):
	
	if request.method == 'GET':
		assets = Asset.objects.all()
		serializer = AssetSerializer(assets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def asset_list_view(request):
    """
    View para renderizar a lista de ativos no frontend Django.
    Busca os dados da API (ou diretamente do banco de dados).
    """
    # Forma 1: Acessar diretamente os objetos do modelo (mais comum para SSR interno)
    assets = Asset.objects.all()
    # Não precisamos serializar aqui se estamos apenas passando os objetos do Django
    # para o template, onde podemos acessar seus atributos diretamente.

    # Forma 2: (Menos comum para SSR interno, mas demonstra como você faria se a API fosse externa)
    # Se você estivesse consumindo uma API REST externa, usaria algo como:
    # import requests
    # api_url = 'http://localhost:8000/api/assets/' # Substitua pela URL real da sua API
    # response = requests.get(api_url)
    # if response.status_code == 200:
    #     assets_data = response.json()
    # else:
    #     assets_data = [] # Ou trate o erro adequadamente

    context = {
        'assets': assets, # Passe os objetos Asset diretamente para o template
    }
    return render(request, 'CRUD/asset_list.html', context)


def CRUD_home(request):
    return render(request, 'CRUD/index.html')

def CRUD_create(request):
    if request.method == "POST":
        received_form = CreateDataForm(request.POST)
        if received_form.is_valid():
            received_form.save()
            return redirect("CRUD:CRUD_home")
    else:
        received_form = CreateDataForm() # Adicionado para exibir o formulário GET
    return render(request, 'CRUD/create.html', {'form': received_form})
	

# def CRUD_home(request):
# 	return render(request, 'CRUD/index.html')

# def CRUD_create(request: HttpRequest):
# 	if request.method == "POST":
# 		received_form = CreateDataForm(request.POST)
# 		if received_form.is_valid():
# 			received_form.save()
# 			return redirect("CRUD:CRUD_home")
# 	form = { 
# 		"form": CreateDataForm()
# 	}
# 	return render(request, 'CRUD/create.html', form)

# def CRUD_retrieve(request: HttpRequest):
# 	if request.method == "GET":
# 		return redirect("CRUD:CRUD_home")
# 	retrieved_data = {
# 		"assets": Asset.objects.all()
# 	}
# 	return render(request, "CRUD/retrieve.html", retrieved_data)

# def CRUD_delete(request:HttpRequest, id:int):
# 	remove_request = get_object_or_404(Asset, id=id)
# 	remove_request.delete()
# 	return redirect("CRUD:CRUD_home")

# def CRUD_update(request:HttpRequest, id:int):
# 	update_request = get_object_or_404(Asset, id=id)
# 	update_form = CreateDataForm(instance=update_request)
# 	if request.method == "POST":
# 		update_form = CreateDataForm(request.POST, instance=update_request)
# 		if update_form.is_valid():
# 			update_form.save()
# 			return redirect("CRUD:CRUD_home")
# 	form = {
# 		"form": update_form
# 	}
# 	return render(request, "CRUD/update.html", form)
# # Create your views here.
