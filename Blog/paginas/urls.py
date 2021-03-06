from django.urls import path

# Importa as views que a gente criou 
from .views import PaginaInicial, PaginaSobre, PaginaAjuda, PaginaInformacao

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
    path('ajuda/', PaginaAjuda.as_view(), name='ajuda'),
    path('informacao/', PaginaInformacao.as_view(), name='informacao'),
    
]