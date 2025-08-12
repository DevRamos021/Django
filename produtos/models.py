from django.utils import timezone

from django.db import models
from django.template.backends import django



class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)

    preco = models.DecimalField(max_digits=10, decimal_places=2)

    descricao = models.TextField(blank=True, null=True)

    estoque = models.IntegerField(default=0)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    promocao = models.BooleanField(default=False)

    data_descricao = models.DateField(default=timezone.now)

    produto = models.CharField(max_length=100)









