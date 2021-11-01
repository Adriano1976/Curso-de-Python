from datetime import datetime, timedelta

data_atual = datetime.strftime(datetime.now(), '%D')
dataAtual = datetime.strftime(datetime.now(), '%d-%m-%Y')
horarioAtual = datetime.strftime(datetime.now(), '%H:%M:%S')

data_hora = datetime(2020, 12, 31, 23, 59, 59)  # Returns date and time according to parameters.
data = data_hora.date()  # Inform only the date.
hora = data_hora.time()  # Inform only the time.

print()
print('-' * 80)
print('----------------------- Date and Time informed by the user ---------------------')
print('-' * 80)

print(f'Data e Hora: {data_hora}')  # Date and time informed by the user.
print(f'Data: {data}')  # Date informed by the user.
print(f'Horas: {hora}')  # Time informed by the user.

print('-' * 80)
print('------------------ Date and Time informed by the Operating System --------------')
print('-' * 80)

print(f'\nData Atual: {data_atual}')  # Date in American format.
print(f'Data Atual: {dataAtual}')  # Date in Brazilian format.
print(f'Hora Atual: {horarioAtual}')  # Time in Brazilian format.

data1 = datetime(2020, 4, 20, 10, 53, 20)
print(data1.strftime('%d/%m/%y %H:%M:%S'))  # Returns date and time in Brazilian format.

print('-' * 80)
print('------------------------ Counting of days and hours ----------------------------')
print('-' * 80)

data2 = datetime.fromtimestamp(1555729200.0)  # Return the date and time informed by the user.
print(f'Data e hora: {data2}')

data3 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
print(f'Data e hora: {data3}')

data4 = data3 + timedelta(days=5, seconds=59)
print(f"Data e hora: {data3.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data e hora: {data4.strftime('%d/%m/%Y %H:%M:%S')}")

data5 = data4 + timedelta(seconds=2 * 60 * 60)
print(f"Data e hora: {data5.strftime('%d/%m/%Y %H:%M:%S')}")

nascNeide = datetime.strptime('21/01/1967 07:21:00', '%d/%m/%Y %H:%M:%S')
nascAdriano = datetime.strptime('12/10/1976 20:41:00', '%d/%m/%Y %H:%M:%S')
print(f"Data de nascimento de Neide: {nascNeide.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data de nascimento de Adriano: {nascAdriano.strftime('%d/%m/%Y %H:%M:%S')}")

dif = nascAdriano - nascNeide
print(f"Diferença de idade: {dif}")
