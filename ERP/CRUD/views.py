from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import CreateDataForm
from .models import AssetModel

def CRUD_home(request):
	return render(request, 'CRUD/index.html')

def CRUD_create(request: HttpRequest):
	if request.method == "POST":
		received_form = CreateDataForm(request.POST)
		if received_form.is_valid():
			received_form.save()
			return redirect("CRUD:CRUD_home")
	form = { 
		"form": CreateDataForm
	}
	return render(request, 'CRUD/create.html', form)

def CRUD_retrieve(request: HttpRequest):
	if request.method == "POST":
		return redirect("CRUD:CRUD_home")
	retrieved_data = {
		"assets": AssetModel.objects.all()
	}
	return render(request, "CRUD/retrieve.html", retrieved_data)

def CRUD_delete(request:HttpRequest, id:int):
	remove_request = get_object_or_404(AssetModel, id=id)
	remove_request.delete()
	return redirect("CRUD:CRUD_home")

def CRUD_update(request:HttpRequest, id:int):
	update_request = get_object_or_404(AssetModel, id=id)
	update_form = CreateDataForm(instance=update_request)
	if request.method == "POST":
		update_form = CreateDataForm(request.POST, instance=update_request)
		if update_form.is_valid():
			update_form.save()
			return redirect("CRUD:CRUD_home")
	form = {
		"form": update_form
	}
	return render(request, "CRUD/update.html", form)
# Create your views here.
