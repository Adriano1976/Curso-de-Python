"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Digite o horário desejado [0 - 23]: ')

try:
    horario.isdigit()  # Verifica se o número é realmente inteiro.
    horario = int(horario)  # Converte uma string em um número inteiro.

    if horario >= 0 and horario <= 11:
        print('Bom dia!\nHorário marcado com sucesso.')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!\nHorário marcado com sucesso.')
    elif horario <= 23:
        print('Boa noite!\nHorário marcado com sucesso.')
    else:
        print('Horário incorreto. Digite o horário entre 0 a 23.')
except:
    print('Digite o horário corretamente.')

print('........................................................')

hora = input('Digite um horário (0-23): ')  # Melhor opção de código.

if hora.isdigit():  # Verifica se o número é realmente inteiro.
     hora = int(hora) # Conberte uma string em um número inteiro.

     if hora < 0 or hora > 23:
         print('horário deve está estre 0 e 23.')
     else:
         if hora <= 11:
             print('Bom dia!\nHorário marcado com sucesso.')
         elif hora <= 17:
             print('Boa tarde!\nHorário marcado com sucesso.')
         else:
             print('Boa noite!\nHorário marcado com sucesso.')
else:
     print('Por favor, digite um horário entre 0 e 23.')