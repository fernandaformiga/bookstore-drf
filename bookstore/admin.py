from django.contrib import admin
from .models import Book, Author


class Authors(admin.ModelAdmin):
    list_display = ('id','name', 'country')
    list_display_links = ('id', 'name')
    search_fields = ('name','country')
    list_per_page = 20

admin.site.register(Author, Authors)

class Books(admin.ModelAdmin):
    list_display = ('id', 'name','genre', 'year')
    list_display_links = ('id', 'name')
    search_fields = ('name','genre')
    list_per_page = 20

admin.site.register(Book, Books)
