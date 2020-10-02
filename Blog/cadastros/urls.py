from django.urls import path

from .views import CategoriaCreate, PostagemCreate, ComentarioCreate, PerfilCreate
from .views import CategoriaUpdate, PostagemUpdate, ComentarioUpdate, PerfilUpdate
from .views import CategoriaDelete, PostagemDelete, ComentarioDelete, PerfilDelete
from .views import CategoriaList, PostagemList, ComentarioList, PerfilList

urlpatterns = [
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('cadastrar/postagem/', PostagemCreate.as_view(), name="cadastrar-postagem"),
    path('cadastrar/comentario/', ComentarioCreate.as_view(), name="cadastrar-comentario"),
    path('cadastrar/perfil/', PerfilCreate.as_view(), name="cadastrar-perfil"),

    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name="editar-categoria"),
    path('editar/postagem/<int:pk>/', PostagemUpdate.as_view(), name="editar-postagem"),
    path('editar/comentario/<int:pk>/', ComentarioUpdate.as_view(), name="editar-comentario"),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name="editar-perfil"),

    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name="excluir-categoria"),
    path('excluir/postagem/<int:pk>/', PostagemDelete.as_view(), name="excluir-postagem"),
    path('excluir/comentario/<int:pk>/', ComentarioDelete.as_view(), name="excluir-comentario"),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name="excluir-perfil"),

    path('listar/categoria/', CategoriaList.as_view(), name="listar-categoria"),
    path('listar/postagem/', PostagemList.as_view(), name="listar-postagem"),
    path('listar/comentario/', ComentarioList.as_view(), name="listar-comentario"),
    path('listar/perfil/', PerfilList.as_view(), name="listar-perfil"),
    
]