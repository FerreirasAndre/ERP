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
	tamplet_name = 'CRUD/consultar_estoque.html'
	context_object_name = 'assets'

@api_view(['GET'])
def CRUD_retrieve(request):
	
	if request.method == 'GET':
		assets = Asset.objects.all()
		serializer = AssetSerializer(assets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def consultar_estoque_view(request):
    """
    View para renderizar a lista de ativos no frontend Django.
    Busca os dados da API (ou diretamente do banco de dados).
    """
    # Forma 1: Acessar diretamente os objetos do modelo (mais comum para SSR interno)
    assets = Asset.objects.all()
    # Não precisamos serializar aqui se estamos apenas passando os objetos do Django
    # para o template, onde podemos acessar seus atributos diretamente.

    context = {
        'assets': assets, # Passe os objetos Asset diretamente para o template
    }
    return render(request, 'CRUD/consultar_estoque.html', context)

def adicionar_estoque_view(request):
    return render(request, 'CRUD/adicionar_estoque.html')

def atualizar_estoque_form_view(request):
    return render(request, 'CRUD/atualizar_estoque_form.html')

def remover_estoque_view(request):
    """
    View para renderizar a página de remoção de estoque.
    """
    # Aqui você pode buscar os ativos ou simplesmente renderizar a página
    assets = Asset.objects.all()  # Busca todos os ativos, se necessário
    context = {
        'assets': assets,  # Passa os ativos para o template, se necessário
    }
    return render(request, 'CRUD/remover_estoque.html', context)

def atualizar_estoque_view(request):
    """
    View para renderizar a página de remoção de estoque.
    """
    # Aqui você pode buscar os ativos ou simplesmente renderizar a página
    assets = Asset.objects.all()  # Busca todos os ativos, se necessário
    context = {
        'assets': assets,  # Passa os ativos para o template, se necessário
    }
    return render(request, 'CRUD/atualizar_estoque.html', context)


def CRUD_home(request):
    return render(request, 'CRUD/index.html')

def CRUD_create(request):
    if request.method == "POST":
        received_form = CreateDataForm(request.POST)
        if received_form.is_valid():
            received_form.save()
            return redirect('CRUD:consultar_estoque')
    else:
        received_form = CreateDataForm() # Adicionado para exibir o formulário GET
    return render(request, 'CRUD/adicionar_estoque.html', {'form': received_form})
    



def CRUD_delete(request, id): # 'id' será o valor capturado da URL
    # Usa get_object_or_404 para buscar o objeto Asset pelo ID
    # Se o objeto não for encontrado, ele automaticamente levanta um 404
    asset_to_delete = get_object_or_404(Asset, pk=id) # 'pk' se refere à chave primária do modelo

    # É uma boa prática verificar o método da requisição para deletes.
    # deletes geralmente são feitos via POST para segurança CSRF.
    # No entanto, para simplicidade inicial e teste, você pode usar GET ou POST.
    # Para o delete simples via link, GET é comum, mas POST é mais seguro.
    # Se for um formulário de confirmação, seria POST.
    if request.method == "POST": # Se você estiver usando um formulário POST para delete
        asset_to_delete.delete()
        return redirect('CRUD:remover_estoque') # Redireciona para a lista de ativos após a exclusão
    
    # Se a requisição não for POST, você pode renderizar uma página de confirmação.
    # Por enquanto, para um delete direto via link, você pode simplificar:
    # (Se você usar um link GET simples no template, remova o 'if request.method == "POST":')
    asset_to_delete.delete() # Exclui o objeto
    return redirect('CRUD:remover_estoque') # Redireciona para a lista de ativos

# ... (suas importações existentes) ...

# Certifique-se de que CRUD_delete está funcionando como esperado

def CRUD_update(request, id): # 'id' será o valor capturado da URL
    # 1. Obter o objeto Asset que será atualizado
    asset_to_update = get_object_or_404(Asset, pk=id) # 'pk' se refere à chave primária (o 'id' numérico agora)

    if request.method == "POST":
        # 2. Quando o formulário é submetido (POST)
        # Cria uma instância do formulário com os dados POST E a instância do objeto existente.
        # Isso permite que o formulário saiba que está "editando" um objeto existente.
        #received_form = CreateDataForm(request.POST, instance=asset_to_update)
        data = request.POST.copy() # Copia os dados do POST para evitar problemas de mutabilidade

        if 'quantity' in data and data['quantity'] == '':
            data['quantity'] = None
        if 'price' in data and data['price'] == '': # Certifique-se de que o nome é 'price' aqui
            data['price'] = None

        received_form = CreateDataForm(data, instance=asset_to_update)
        
        if received_form.is_valid():
            received_form.save() # Salva as alterações no objeto existente
            return redirect('CRUD:consultar_estoque') # Redireciona para a lista de ativos após a atualização
        else:
            # Se o formulário não for válido, renderize o template com os erros
            print("Erro ao tentar realizar atualização:", received_form.errors) # Para depuração no console
            return render(request, 'CRUD/atualizar_estoque.html', {'form': received_form}) # Reutiliza o template de adicionar
    else:
        # 3. Quando a página é acessada pela primeira vez (GET)
        # Cria uma instância do formulário preenchida com os dados do objeto existente.
        received_form = CreateDataForm(instance=asset_to_update)
    
    # 4. Renderiza o template do formulário (preenchido para GET, ou com erros para POST inválido)
    return render(request, 'CRUD/atualizar_estoque_form.html', {'form': received_form})