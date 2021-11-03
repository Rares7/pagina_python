from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField("Genero", max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Fallecido', null=True, blank=True)


class Book(models.Model):
    '''Libro para aplicación de biblioteca ...'''
    title = models.CharField(max_length=250)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    fecha = models.DateField(blank=True, null=True, help_text='Fecha de publicación')

    #faltan relaciones
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self) :
        return self.title

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:2] ])
    display_genre.short_description = 'Genre'