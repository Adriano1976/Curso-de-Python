from time import sleep

print('-------------------------------------------------------------------')

months = ['Janeiro', 'Fevereiro', 'Marça', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
          'Outubro', 'Novembro', 'Dezembro']

iterator = iter(months)

while True:
    try:
        month = next(iterator)
        print(month)
        sleep(1.0)
    except StopIteration:
        break
