from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponse
from catalogo.models import Book
from catalogo.forms import AuthorForm

# Create your views here.
def indice(request):
    '''
    Pagina inicial de nuestra web
    '''
    datos = {'autor': 'Rares'}
    
    busqueda = request.GET.get('q')
    if busqueda:
        libros = Book.objects.filter(title__icontains=busqueda)
        datos['noencontrado'] = True
    else:
        libros = Book.objects.all()

    datos['libros'] = libros

   
    return render(request, 'index.html', context=datos)

def contacto(request):
    contacto = {'nombre': 'Rares Mogojan', 'email': 'correo@contacto.com', 'telefono': '976521308'} 

    return render(request, 'contacto.html', context=contacto)

def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    return render(request, 'todos_libros.html', context={'libros': libros})

def crear_autor(request):
    datos = {'form': AuthorForm()}
    return render(request, 'crear_autor.html', context=datos)

class LibrosListView(generic.ListView):
    '''
    Vista generica para nuestro listado de libros
    '''
    model = Book
    paginated_by = 25

class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'libros/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query)