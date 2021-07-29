from calendar import monthrange
from datetime import datetime


# Returns a tuple containing the number of the day in the week (0-6) and the last day of February 2020.
print(f'February 2021: {monthrange(2021, 2)}')
print(f'February 2005: {monthrange(2021, 2)}')
print(f'February 1976: {monthrange(2021, 2)}')
print(f'February 1967: {monthrange(2021, 2)}')

# Output - (5, 29).
# The 5 means it's a Saturday.
# The 29th means this is the last day of the month.

dia_semana, ultimio_dia = monthrange(1976, 2)
print(f'Dia da semana: {dia_semana + 1}')
print(f'Último dia de Fevereiro: {ultimio_dia}')

# Last days of months of the year informed.
ultimos = [monthrange(datetime.now().year, m)[1] for m in range(1, 13)]
print(f'Last days of months of the year informed: {ultimos}')
