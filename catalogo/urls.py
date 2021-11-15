from django.urls import path, include
from catalogo.views import crear_autor

urlpatterns = [
#   path('libros/', views.LibrosListView.as_view(), name='listado_libros'),
#   path('buscar/', SearchResultsListView.as_view(), name="buscalibros"),
    path('autor/create', crear_autor, name='crear_autor')
]