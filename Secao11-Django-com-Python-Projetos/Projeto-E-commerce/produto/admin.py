"""
- Percebi que se não cadastrar uma variação para o produto, (nem mesmo os valores) o select fica em branco e
provavelmente vai dar pau la na frente quando formos pegar essa info e continuar o projeto.
- Nesse caso pensei em fazer o seguinte, caso o usuário deixe em branco os campos da variação,
como faço no models para definir ao menos uma variação que irá receber o nome e os valores do produto?
- Agora você precisa criar um arquivo chamado de "forms.py" em produto (pode ter qualquer nome que quiser,
mas se copiar meu código é forms.py). E pronto, agora cada produto vai precisar ter pelo menos uma variação.
"""

from django.contrib import admin
from .models import Produto, Variacao
from .forms import VariacaoObrigatoria


class VariacaoInLine(admin.TabularInline):
    model = Variacao
    formset = VariacaoObrigatoria
    min_num = 1
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [VariacaoInLine]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
