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
	# path("delete/<int:id>", views.CRUD_delete, name="CRUD_delete"),
	# path("update/<int:id>", views.CRUD_update, name="CRUD_update"),
    path('list_assets/', views.asset_list_view, name='asset_list'),
    path('api/', include(router.urls)),

]