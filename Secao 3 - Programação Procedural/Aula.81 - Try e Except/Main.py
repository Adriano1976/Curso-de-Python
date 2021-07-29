try:
    a = {}
    print(a[1])
except NameError as erro:
    print(f'Erro: {erro}.')
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado')

print('Bora continuar...')
