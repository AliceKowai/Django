from django.contrib import admin
from .models import Livros

class ListLivros(admin.ModelAdmin):
    list_display = ('titulo_livro', 'capa_imagem', 'ano_publicacao','quantidade_paginas','autor','editora', 'preco')

admin.site.register(Livros, ListLivros)
