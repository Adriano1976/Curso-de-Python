"""
Exemplo do uso das seguintes funções:
startwith - Buscar o nome ou letra inicial em uma determinada lista.
lower - Converte uma string para menuscula.
upper - Converte uma string para maiuscula.
"""

variavel = ['Luiz Otávio', 'João de Barro', 'Maria do Carmo', 'Adriano Santos',
            'Maria Ferreira', 'Algusto Vasconcelos', 'Adailton Ferreira']

nomeProcurado = input('Digite o nome desejado: ')
nomeEcontrado = False
nome = []

for nome in variavel:
    if nome.lower().startswith(nomeProcurado) or nome.upper().startswith(nomeProcurado):
        nomeEcontrado = True
        print(nome)

if not nomeEcontrado:
    if len(nomeProcurado) <= 1:
        print(f'Nome com a letra "{nomeProcurado}" não encontrado.')
    else:
        print(f'Nome "{nomeProcurado}" não encontrado.')
