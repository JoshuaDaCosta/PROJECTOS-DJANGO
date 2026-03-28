from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("posts/", views.listar_post, name="listar_post"),
    path("post/", views.salvar_post, name="salvar_post"),
    path("editar/<int:id>/", views.editar_post, name="editar_post"),
    path("deletar/<int:id>/", views.deletar_post, name="deletar_post"),
]
