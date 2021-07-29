"""
Faça um programa que efetue o cálculo e a apresentação do valor de uma prestação em atraso.
"""

cont = 0
while True:

    # Entradas de dados
    valor = input('Digite o valor da prestação: R$ ')
    diaAtraso = input('Digite os dias de atraso: ')
    taxa = input('Digite a taxa cobrado ao mês: ')

    try:
        # Processamento de dados
        valor.isdigit()
        valor = float(valor)
        diaAtraso.isdigit()
        diaAtraso = float(diaAtraso)
        taxa.isdigit()
        taxa = float(taxa)

        # Cálculo do novo valor da prestação.
        novoValor = valor + (valor * (((taxa / 100) / 30) * diaAtraso))

        # Saída de dados processado
        print(f'Novo valor da prestação: R$ {novoValor:.2f}')

        sair = input('Deseja Sair? [S - N]: ')
        if sair == 's':
            print('Pragrama encerrando...')
            break
        elif sair == 'n':
            print('')
            continue
        else:
            print('Resposta Incorreta.\nPrograma encerrando...')
            break

    except:

        # Processamento e saída de dados
        print('Valor Incorreto. Tente Novamente\n.')
        continue

        sair = input('Deseja Sair? [S - N]: ')
        if sair == 's':
            print('Programa encerrando...')
            break
        elif sair == 'n':
            print('')
            continue
        else:
            print('Resposta Incorreta.\nPrograma encerrando...')
            break

    cont += 1