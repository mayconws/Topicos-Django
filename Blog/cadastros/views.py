from django.views.generic.edit import CreateView, UpdateView

from .models import Categoria, Postagem, Comentario, Perfil

from django.urls import reverse_lazy

# Create your views here.
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PostagemCreate(CreateView):
    model = Postagem
    fields = ['titulo', 'data', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ComentarioCreate(CreateView):
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'comentario_publicado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#### Update ####

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PostagemUpdate(UpdateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ComentarioUpdate(UpdateView):
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'comentario_publicado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')



    

