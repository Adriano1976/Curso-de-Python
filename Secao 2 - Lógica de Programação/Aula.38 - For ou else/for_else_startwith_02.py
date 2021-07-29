"""
Exemplo do uso das seguintes funções:
startwith - Buscar o nome ou letra inicial em uma determinada lista.
upper - Converte uma string para maiuscula.
"""

variavel = ['Luiz Otávio', 'João de Barro', 'Maria do Carmo', 'Adriano Santos',
            'Maria Ferreira', 'Algusto Vasconcelos', 'Adailton Ferreira']

nomeProcurado = input('Digite o nome procurado: ').upper()

encontrado = [nome for nome in variavel if nome.startswith(nomeProcurado)]

print(f'Nome(s) encontrado(s): {encontrado}.')
