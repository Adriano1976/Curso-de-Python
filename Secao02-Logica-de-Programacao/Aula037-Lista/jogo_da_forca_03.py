print('**********************************')
print('*** Bem Vindo ao Jogo da Forca ***')
print('**********************************')

secreto = ['P', 'E', 'R', 'F', 'U', 'M', 'E']
digitadas = []
tentativas = 3

while True:

    if tentativas <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ').upper()

    if len(letra) > 1:
        print('Digite SOMENTE 1 letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO existe na palavra secreta.')
        digitadas.pop()

    letra_secreta = ''

    for i in secreto:
        if i in digitadas:
            letra_secreta += i
        else:
            letra_secreta += ' _ '

    if letra_secreta == ''.join(secreto):
        print(f'Você ganhou, pois a palara era {letra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {letra_secreta}')

    if letra not in secreto:
        tentativas -= 1

    print(f'Você tem {tentativas} tentativas.')
    print('')
