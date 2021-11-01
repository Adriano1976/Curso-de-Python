print('**********************************')
print('*** Bem Vindo ao Jogo da Forca ***')
print('**********************************')

secreta = 'perfume'
digitadas = []
tentativas = 3

while True:
    if tentativas <= 0:
        print('Você Perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'A letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for i in secreta:
        if i in digitadas:
            secreto_temporario += i
        else:
            secreto_temporario += ' _ '

    if secreto_temporario == secreta:
        print(f'Você ganhou, pois a palavra era [{secreto_temporario.upper()}].')
        break
    else:
        print(f'A palavra secreta está assim: [{secreto_temporario.upper()}].')

    if letra not in secreta:
        tentativas -= 1

    print(f'Você ainda tem {tentativas} tentativas.')
    print('')
