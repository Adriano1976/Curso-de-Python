"""
Faça um programa que leia uma temperatura em grau Celsius e aprentá-la convertida em graus Fahrenheit.
"""

# Entrada de dados
celsius = input('Digite a temperatura em Celsius: ')

try:
    # Processamento de dado
    celsius.isdigit() # Confere se o valor digita foi um número.
    celsius = float(celsius) # Converte uma string para um número flutuante.
    fahrenheit = ((9 * celsius) + 160) / 5

    # Saída de dados
    print(f'Temperatura: {fahrenheit} F°')

except:

    # Saída de dados
    print(f'Valor ifgnválido. Digite a temperatura corretamente')