"""
- Comma Separated Values - CSV (Valores separados por vírgula).
- É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r', encoding='utf8', newline='') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
    # DictReader - Used to open a csv file in the form of an ordered dictionary.

    for dado in dados:
        print(dado)

with open('clientes01.csv', 'w', encoding='utf8', newline='') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )
