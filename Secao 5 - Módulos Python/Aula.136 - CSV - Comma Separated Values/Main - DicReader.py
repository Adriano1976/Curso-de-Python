"""
- Comma Separated Values - CSV (Valores separados por vírgula).
- É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
    # DictReader - Used to open a csv file in the form of an ordered dictionary.

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar="",
        quoting=csv.QUOTE_ALL
    )

    for dado in dados:
        escreve.writerow(
            dado['Nome'],
            dado['Sobrenome'],
            dado['E-mail'],
            dado['Telefone']
        )