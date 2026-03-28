from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_livros, name="listar_livros"),
    path("adicionar/", views.postar_livros, name="postar_livros"),
    path("deletar/<int:id>", views.deletar_livros, name="deletar_livros"),
    path("editar/<int:id>", views.editar_livros, name="editar_livros"),
]
