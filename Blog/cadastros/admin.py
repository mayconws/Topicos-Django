from django.contrib import admin

# Importar Classes
from .models import Categoria, Postagem, Comentario, Perfil

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(Perfil)