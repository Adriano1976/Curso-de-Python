"""
* Criar variável para nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int).
* Obter o ano de nascimento da pessoa ()
"""

nome = 'Adriano'
idade = 45
altura = 1.85
peso = 72.5
anoAtual = 2021
anoNascimento = anoAtual - idade
indiceMassaCorpotal = peso / (altura ** 2)
print('..............................................................')
print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} kg e o seu IMC é {indiceMassaCorpotal:.2f}.')
print(f'{nome} nasceu em {anoNascimento}.')
print('..............................................................')
