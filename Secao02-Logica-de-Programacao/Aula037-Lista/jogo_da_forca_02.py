print('**********************************')
print('*** Bem Vindo ao Jogo da Forca ***'.upper())
print('**********************************\n')

palavra_secreta = 'perfume'
letras_acertadas = ['_', '_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while not enforcou and not acertou:

    chute = input('Digite uma letra: ')

    if len(chute) > 1:
        print('Não valeu, pois digitou mais de uma letra.')
        continue

    print(f'Você digitou a letra {chute}.\n')

    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta.upper():
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')

print('Fim do Jogo')