def funcao_decoradora(funcao_decorada):
    def funcao_interna(*args, **kwargs):
        print('Posso fazer algo antes de executar a função')
        resultado_funcao_decorada = funcao_decorada(*args, **kwargs)
        print('Posso fazer algo depois de executar a função')

        try:
            # Vou adicionar coisas na função
            resultado_funcao_decorada.append('ISSO VEIO DO DECORADOR')
        except AttributeError:
            ...

        return resultado_funcao_decorada

    return funcao_interna


@funcao_decoradora
def nome_de_clientes():
    nomes = ['Luiz', 'Maria', 'João']
    return nomes


print(nome_de_clientes())

"""
Saída:
Por fazer algo antes de executar a função
Posso fazer algo depois de executar a função
['Luiz', 'Maria', 'João', 'ISSO VEIO DO DECORADOR']
"""
