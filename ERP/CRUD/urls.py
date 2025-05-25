from django.urls import path
from . import views

app_name = "CRUD"

urlpatterns = [
	path("", views.CRUD_home, name="CRUD_home"),
	path("create/", views.CRUD_create, name="CRUD_create"),
	path("retrieve/", views.CRUD_retrieve, name="CRUD_retrieve"),
	path("delete/<int:id>", views.CRUD_delete, name="CRUD_delete"),
	path("update/<int:id>", views.CRUD_update, name="CRUD_update")
]