from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "CRUD"

router = DefaultRouter()
router.register('assets', views.AssetViewSet)

urlpatterns = [
	path("", views.CRUD_home, name="CRUD_home"),
	path("create/", views.CRUD_create, name="CRUD_create"),
	path("retrieve/", views.CRUD_retrieve, name="CRUD_retrieve"),
	path("delete/<int:id>", views.CRUD_delete, name="CRUD_delete"),
	path("update/<int:id>", views.CRUD_update, name="CRUD_update"),
    path('consultar_estoque/', views.consultar_estoque_view, name='consultar_estoque'),
	path('adicionar_estoque/', views.adicionar_estoque_view, name='adicionar_estoque'),
    path('remover_estoque/', views.remover_estoque_view, name='remover_estoque'),
    path('atualizar_estoque/', views.atualizar_estoque_view, name='atualizar_estoque'),
    path('atualizar_estoque_form/', views.atualizar_estoque_form_view, name='atualizar_estoque_form'),
	path('api/', include(router.urls)),

]