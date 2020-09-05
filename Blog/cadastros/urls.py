from django.urls import path

from .views import CategoriaCreate, PostagemCreate, ComentarioCreate, PerfilCreate
from .views import CategoriaUpdate, PostagemUpdate, ComentarioUpdate, PerfilUpdate

urlpatterns = [
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('cadastrar/postagem/', PostagemCreate.as_view(), name="cadastrar-postagem"),
    path('cadastrar/comentario/', ComentarioCreate.as_view(), name="cadastrar-comentario"),
    path('cadastrar/perfil/', PerfilCreate.as_view(), name="cadastrar-perfil"),

    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name="editar-categoria"),
    path('editar/postagem/<int:pk>/', CategoriaUpdate.as_view(), name="editar-postagem"),
    path('editar/comentario/<int:pk>/', ComentarioUpdate.as_view(), name="editar-comentario"),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name="editar-perfil"),
    
]