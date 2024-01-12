# Generated by Django 5.0.1 on 2024-01-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_livro', models.CharField(max_length=100)),
                ('capa_imagem', models.CharField(max_length=1000)),
                ('ano_publicacao', models.IntegerField(max_length=350)),
                ('quantidade_paginas', models.IntegerField(max_length=60)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('preco', models.FloatField(default=0.0)),
            ],
        ),
    ]