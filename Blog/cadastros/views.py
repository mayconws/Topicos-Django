from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Categoria, Postagem, Comentario, Perfil

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Categoria"
        context['botao'] = "Cadastrar"

        return context


class PostagemCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Usuário"]
    model = Postagem
    fields = ['titulo', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Postagem"
        context['botao'] = "Cadastrar"

        return context

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url


class ComentarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['nome_comentario', 'email', 'postagem', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Comentário"
        context['botao'] = "Cadastrar"

        return context


class PerfilCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'email_perfil', 'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Perfil"
        context['botao'] = "Cadastrar"

        return context

#### Update ####


class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de Categoria"
        context['botao'] = "Salvar"

        return context


class PostagemUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Postagem
    fields = ['titulo', 'conteudo', 'imagem', 'postado', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-postagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de Postagem"
        context['botao'] = "Salvar"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Postagem, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['nome_comentario', 'email', 'postagem', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de Comentário"
        context['botao'] = "Salvar"

        return context


class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome_perfil', 'endereco', 'email_perfil',
              'cpf', 'telefone', 'imagem_perfil']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-perfil')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de Perfil"
        context['botao'] = "Salvar"

        return context

#### Delete ####


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')


class PostagemDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Postagem
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-postagem')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Postagem, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ComentarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
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

    def get_queryset(self):
        self.object_list = Postagem.objects.filter(usuario=self.request.user)
        return self.object_list


class ComentarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'cadastros/listas/comentario.html'


class PerfilList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'
