"""
Faça um programa que receba a temperatura em Fahrenheit, converta para Celsius e impriva a temperatura convertida.
"""
fahrenheit = input('Digite a temperatura em F° [xx.xx]: ')

try:
    fahrenheit.isdigit()
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5 / 9)

    print(f'Temperatura: {celsius:.2f} C°')
except:
    print('Valor incorreto.\nDigite corretamente.')
