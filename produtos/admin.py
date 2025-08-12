from django.contrib import admin
from .models import Categoria,Produto
from django.utils.html import format_html


@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nome',)


@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'categoria',
        'preco',
        'estoque',
        'promocao',

    )

    list_filter = ('categoria', 'promocao')

    search_fields = ('nome', 'descricao')


