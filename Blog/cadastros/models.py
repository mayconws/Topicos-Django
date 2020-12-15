from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name="Nome da Categoria")

    def __str__(self):
        return "{}".format(self.nome_categoria)

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    data = models.DateField(auto_now=True)
    conteudo = models.TextField()
    imagem = models.ImageField()
    postado = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.titulo)

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField()
    data = models.DateField(auto_now=True)
    comentario = models.TextField()
    comentario_publicado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    postagem = models.ForeignKey(Postagem, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome_comentario)

class Perfil(models.Model):
    nome_perfil = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=150, verbose_name="Endereço")
    email_perfil = models.EmailField(verbose_name="Email", unique=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    imagem_perfil = models.ImageField(verbose_name="Imagem", null=True, blank=True, default="Nenhuma Imagem")

    def __str__(self):
        return "{}".format(self.nome_perfil)




