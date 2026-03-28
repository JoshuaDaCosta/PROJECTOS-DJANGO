from django.db import models

# Create your models here.


# class Cliente(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     telefone = models.CharField(max_length=20)
#     empresa = models.CharField(max_length=100, blank=True)

# class Interacao(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     data = models.DateTimeField(auto_now_add=True)
#     anotacao = models.TextField()

# aula_crm django

# class CLIENTE(models.Model):
#     nome=models.CharField(max_length=100)
#     email=models.EmailField()
#     telefone = models.CharField(max_length=20)
#     empresa = models.CharField(max_length=100, blank=True)
#     activo = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nome #def __str__(self): é um método especial em Python que retorna uma representação em string do objeto. No caso do modelo CLIENTE, ele retorna o valor do campo nome, o que facilita a identificação dos objetos CLIENTE quando eles são exibidos em interfaces administrativas ou em outras partes do código.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    empresa = models.ForeignKey(
        "Empresa", null=True, blank=True, on_delete=models.SET_NULL
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class interacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_interacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interação com {self.Cliente.nome} em {self.data_interacao.strftime('%Y-%m-%d %H:%M:%S')}"


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
