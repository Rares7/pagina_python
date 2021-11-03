from django.shortcuts import render
# from django.http import HttpResponse
from catalogo.models import Book

# Create your views here.
def indice(request):
    '''
    Pagina inicial de nuestra web
    '''
    libros = Book.objects.all()
    datos = {'autor': 'Rares', 'libros':libros}
    return render(request, 'index.html', context=datos)
