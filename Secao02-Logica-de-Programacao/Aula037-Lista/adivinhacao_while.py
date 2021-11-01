print('**********************************')
print('****   Jogo da Adivinhação    ****')
print('**********************************')

numero_secreto = 42
tentativas = 3
contador = 1

while contador <= tentativas:
    print(f'Tentativa {contador} de {tentativas}.')

    chute = int(input('Digite o seu número: '))
    print('Você digitou:', chute, )

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
  
    if acertou:
        print('Você acertou!\n')
        break
    elif maior:
        print('Você ERROU, pois seu chute foi maior que o número secreto.\n')
    elif menor:
        print('Você ERROU, pois seu chute foi menor que o número secreto.\n')

    contador += 1

print('Fim do jogo!!')
