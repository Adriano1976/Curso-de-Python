def formata_preco(valor):
    try:
        import locale
        valor_int = float(valor)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(valor_int, grouping=True)

        # return f'R$ {valor:.2f}'.replace('.', ',')
        return valor_formatado
    except ValueError:
        # Trate o erro
        raise


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()
        ]
    )
