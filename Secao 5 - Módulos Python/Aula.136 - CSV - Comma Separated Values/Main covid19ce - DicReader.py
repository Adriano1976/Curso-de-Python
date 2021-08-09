"""
- Comma Separated Values - CSV (Valores separados por vírgula).
- É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import csv

with open('Casos escalados de covid19.csv', 'r', newline='') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
    # DictReader - Used to open a csv file in the form of an ordered dictionary.

    for dado in dados:
        print(dado)

with open('ce - covid19aracaju.csv', 'w', newline='', encoding='UTF-8') as arquivo:
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
            chaves[7],
            chaves[8],
            chaves[9],
            chaves[10],
            chaves[11],
            chaves[12],
            chaves[13],
            chaves[14],
            chaves[15],
            chaves[16],
            chaves[17],
            chaves[18],
            chaves[19],
            chaves[20]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Código'],
                dado['Data'],
                dado['Cidade'],
                dado['Casos Confirmados'],
                dado['Casos Confirmados de Hoje'],
                dado['Pessoas Internadas'],
                dado['Pessoas Internadas Hoje'],
                dado['Pessoas Isoladas'],
                dado['Pessoas Isoladas Hoje'],
                dado['Pessoas Curadas'],
                dado['Pessoas Curadas Hoje'],
                dado['Óbitos'],
                dado['Óbitos de Hoje'],
                dado['Casos Suspeitos'],
                dado['Suspeitos Isolados'],
                dado['Suspeitos Internados'],
                dado['Óbitos Investigados'],
                dado['Casos Descartados'],
                dado['Casos Testados'],
                dado['Casos Testados Hoje'],
                dado['Estado']
            ]
        )
