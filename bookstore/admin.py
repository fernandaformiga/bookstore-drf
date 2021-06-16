from django.contrib import admin
from .models import Book, Author


class Author(admin.ModelAdmin):
    list_display = ('id','name', 'country')
    list_display_links = ('id', 'name')
    search_fields = ('name','country')
    list_per_page = 20

# admin.site.register(Author, Authors)

class Book(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

# admin.site.register(Book, Books)