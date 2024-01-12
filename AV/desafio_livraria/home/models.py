from django.db import models

class Livros(models.Model):
    titulo_livro = models.CharField(max_length=100)
    capa_imagem = models.URLField(max_length=1000)
    ano_publicacao = models.IntegerField()
    quantidade_paginas = models.IntegerField()
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.titulo_livro
    
