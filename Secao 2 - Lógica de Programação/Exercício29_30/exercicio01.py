"""
Faça um programa que peça ao usuário para digitar um número inteiro,
Informe se este número é par ou ímpar. caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try:
    num.isdigit()  # Verifica se o número digitado é realmente um número inteiro.
    num = int(num)  # Converte uma string para um número inteiro.
    if num % 2 == 0: # Verifica se o resto da divisão da variável por 2 é 0 ou 1.
        print(f'Esse número: {num} é PAR.')
    else:
        print(f'Esse número: {num} é IMPAR.')

except:
    print('Isso não é um número inteiro.')

print('...........................................')

numero_inteiro = input('Digite um número inteiro: ')  # Melhor Opção de Código

if numero_inteiro.isdigit():  # Verifica se o número digitado é realmente um número inteiro.
    numero_inteiro = int(numero_inteiro)  # Converte uma string para um número inteiro.

    if numero_inteiro % 2 == 0: # Verifica se o resto da divisão de uma variável é 0 ou 1.
        print(f'{numero_inteiro} é par.')
    else:
        print(f'{numero_inteiro} é impar.')

else:
    print('isso não é um número inteiro.')

print('.............................................')

numero_int = input('Digite um número inteiro: ')

if not numero_int.isdigit():
    print('Isso não é um número inteiro.')
else:
    numero_int = int(numero_int)

    if not numero_int % 2 ==0:
        print(f'{numero_int} é ímpar.')
    else:
        print(f'{numero_int} é par.')