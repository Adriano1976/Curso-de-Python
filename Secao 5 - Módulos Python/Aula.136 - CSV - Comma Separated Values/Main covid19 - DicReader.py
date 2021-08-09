"""
- Comma Separated Values - CSV (Valores separados por vírgula).
- É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import csv

with open('Casos Diários de Covid-19.csv', 'r', newline='') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
    # DictReader - Used to open a csv file in the form of an ordered dictionary.

    for dado in dados:
        print(dado)

with open('Casos Diários de Coronarirus.csv', 'w', newline='') as arquivo:
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
            chaves[3],
            chaves[4],
            chaves[5],
            chaves[6],
            chaves[7]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Código'],
                dado['Cidade'],
                dado['Descrição'],
                dado['Casos'],
                dado['Percentual'],
                dado['Fator'],
                dado['%'],
                dado['Estado']
            ]
        )
