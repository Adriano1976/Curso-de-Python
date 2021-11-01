meses = ['janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
n = 1

while n < 4:
    mes = int(input('Escolha um mês (1-12): '))
    if 1 <= mes < 13:
        print(f'O mês é {meses[mes - 1]}')
