from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Categoria, Postagem, Comentario, Perfil

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.
class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    model = Postagem
    fields = ['titulo', 'data', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'postagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'email_perfil', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

#### Update ####

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    model = Postagem
    fields = ['titulo', 'data', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['nome_comentario', 'email', 'data', 'postagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'email_perfil', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

#### Delete ####

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class PostagemDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Admnistrador"
    model = Postagem
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-postagem')

class ComentarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comentario')

class PerfilDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-perfil')

#### Listar ####

class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

class PostagemList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Postagem
    template_name = 'cadastros/listas/postagem.html'

class ComentarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'cadastros/listas/comentario.html'

class PerfilList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'
