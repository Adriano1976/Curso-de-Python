from calendar import mdays, monthrange
from datetime import datetime
from locale import setlocale, LC_ALL

# Inform Pycharm which date and time should be in the Brazilian standard.
# Can be used 'Portuguese_Brazil.1252' or 'pt_BR.utf-8' in Windows system.
setlocale(LC_ALL, 'pt_BR.utf-8')

# Inform the current date in American format.
data = datetime.now()
print(f'Data: {data}')

# Date and time in Brazilian standard and formatted.
formatacao1 = data.strftime('%A, %d de %B de %Y')
print(f'Data: {formatacao1}')

# Date and time in Brazilian standard and formatted.
formatacao2 = data.strftime('%d/%m/%Y %H:%M:%S')
print(f'Data: {formatacao2}')

# Inform the current month and how many days it has.
mes_atual = int(data.strftime('%m'))
print(f'Mês {mes_atual} tem {mdays[mes_atual]} dias.')

#  Inform the last day of each month of the year.
ultimos = [monthrange(datetime.now().year, m)[1] for m in range(1, 13)]
print(ultimos)
