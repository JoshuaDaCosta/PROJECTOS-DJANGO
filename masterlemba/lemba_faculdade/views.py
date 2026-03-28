from django.shortcuts import *
from .models import *
from .forms import PostForm


def lista_clientes(request):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        cliente.primeiro_e_ultimo_nome = (
            f"{cliente.nome.split()[0]} {cliente.nome.split()[-1]}"
        )
    return render(
        request, "lemba_faculdade/lista_clientes.html", {"clientes": clientes}
    )


def salvar_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")
        post = Post(titulo=titulo, conteudo=conteudo)
        post.save()
        return redirect("listar_post")  # redireciona depois de salvar
    return render(request, "exe1/index.html")


def listar_post(request):
    posts = Post.objects.all()
    return render(request, "exe1/mostrar.html", {"posts": posts})


def editar_post(request, id):
    # Pega o post ou dá 404
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("salvar_post")
    else:
        # Se for GET, criamos o form com os dados existentes do post
        form = PostForm(instance=post)

    # Aqui o form SEMPRE existe, nunca vai dar UnboundLocalError
    return render(request, "exe2/editar.html", {"form": form})


def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("listar_post")
