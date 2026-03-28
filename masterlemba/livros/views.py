from django.shortcuts import *
from .models import Livros
from .forms import LivroForm


# Create your views here.
def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, "listar_livros.html", {"livros": livros})


def postar_livros(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm()
    return render(request, "adicionar.html", {"form": form})


def deletar_livros(request, id):
    post = get_object_or_404(Livros, id=id)
    post.delete()
    return redirect("listar_livros")


def editar_livros(request, id):
    livro = get_object_or_404(Livros, id=id)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm(instance=livro)
    return render(request, "editar.html", {"form": form})
