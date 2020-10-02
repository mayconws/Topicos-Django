from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Categoria, Postagem, Comentario, Perfil

from django.urls import reverse_lazy

# Create your views here.
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemCreate(CreateView):
    model = Postagem
    fields = ['titulo', 'data', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioCreate(CreateView):
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'comentario_publicado', 'postagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

#### Update ####

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemUpdate(UpdateView):
    model = Postagem
    fields = ['titulo', 'data', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioUpdate(UpdateView):
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'comentario_publicado', 'postagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

#### Delete ####

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemDelete(DeleteView):
    model = Postagem
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioDelete(DeleteView):
    model = Comentario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfil')

#### Listar ####

class CategoriaList(ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

class PostagemList(ListView):
    model = Postagem
    template_name = 'cadastros/listas/postagem.html'

class ComentarioList(ListView):
    model = Comentario
    template_name = 'cadastros/listas/comentario.html'

class PerfilList(ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'
