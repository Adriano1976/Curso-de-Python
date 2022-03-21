from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInLine]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
