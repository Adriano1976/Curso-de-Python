"""
Documentação e funções "built-in" úteis.
Verificação se os números são inteiros ou não.
"""
print('......................................')

num01 = input('Digite um número: ')
num02 = input('Digite um número: ')
if num01.isdigit() and num02.isdigit():
    print('Os dois são números inteiros.')
else:
    print('Un deles não é número inteiro.')

print('......................................')
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
if num1.isdecimal() and num2.isdecimal():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não pude converter os números para realizar contas.')

print('......................................')

num3 = input('Digite um número: ')
num4 = input('Digite um número: ')

try:
    num3 = float(num3)
    num4 = float(num4)
    print(num3 + num4)

except:
    print('EEROR.')

print('......................................')

numero = input("Digite um número: ")  # string

try:
    numero_flutuante = float(numero.replace(',', '.'))
    print('Realmente é um número que pode ser de ponto flutuante', numero_flutuante)
except ValueError:
    print('Não é um número')

print('......................................')

