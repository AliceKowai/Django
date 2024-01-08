from django.db import models
#pasta sempre vai ser no plural e a class é no singular
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=30)