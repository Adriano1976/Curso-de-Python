from datetime import datetime

ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
hora_atual = int(datetime.strftime(datetime.now(), '%H'))
min_atual = int(datetime.strftime(datetime.now(), '%M'))
seg_atual = int(datetime.strftime(datetime.now(), '%S'))

data_atual = datetime.strftime(datetime.now(), '%D')
dataAtual = datetime.strftime(datetime.now(), '%d-%m-%Y')
horarioAtual = datetime.strftime(datetime.now(), '%H:%M:%S')

data_hora = datetime(2020, 12, 31, 23, 59, 59)  # Retorna a data e as horas de acordo com os parámetros.
data = data_hora.date()
hora = data_hora.time()

print()
print('-' * 80)
print('----------------------- Data e Hora informada pelo usuário ---------------------')
print('-' * 80)
print(f'Data e Hora: {data_hora}')
print(f'Data: {data}')
print(f'Horas: {hora}')
print('-' * 80)
print('------------------ Data e Hora informado pelo Sistema Operacional --------------')
print('-' * 80)
print(f'Ano Atual: {ano_atual}')
print(f'Hora Atual: {hora_atual}')
print(f'Minuto Atual: {min_atual}')
print(f'Segundo Atual: {seg_atual}')

print(f'\nData Atual: {data_atual}')
print(f'Data Atual: {dataAtual}')
print(f'Hora Atual: {hora_atual}:{min_atual}:{seg_atual}')
print(f'Hora Atual: {horarioAtual}')
