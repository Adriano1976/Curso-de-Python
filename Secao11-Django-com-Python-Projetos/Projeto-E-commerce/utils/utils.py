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


