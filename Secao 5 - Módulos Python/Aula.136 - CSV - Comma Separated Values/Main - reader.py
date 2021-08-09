"""
- Comma Separated Values - CSV (Valores separados por vírgula).
- É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""

import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    # Reader - Used to open a csv file in the form of a simplified dictionary.
    next(dados)

    for dado in dados:
        print(dado)
