'''
While / Else / Contadores e acumuladores
'''
contador = 1
acumulador = 1
while contador <= 10:
    print(f'Contador: {contador} | Acumulador: {acumulador }.')

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')