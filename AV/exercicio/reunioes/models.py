from django.db import models

class Reuniao(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField()
    local = models.CharField(max_length=100,blank=False, null=False)
    nome_do_participante = models.CharField(max_length=100, blank=False, null=False)
    dia_hora = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
