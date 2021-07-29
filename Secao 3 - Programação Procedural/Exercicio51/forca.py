def jogar():
    print('------------------------------------')
    print('|    BEM VINDO AO JOGO DA FORCA    |')
    print('------------------------------------')

    palavra_secreta = ['P', 'E', 'R', 'F', 'U', 'M', 'E']
    digitadas = []
    acertou = False
    tentativas = 3

    for i in range(0, len(palavra_secreta)):
        digitadas.append('_')

    print(f'|    DESCUBRA A PALAVRA SECRETA    |\n{digitadas}')

    while acertou == False:

        if tentativas <= 0:
            print('Você perdeu.')
            break

        print(f'Você tem {tentativas} tentativas no jogo.')
        letra = input('Digite um letra: ').upper()

        if len(letra) > 1:
            print('Mais de 1 letras não vale.')
            print(f'\n|    DESCUBRA A PALAVRA SECRETA    |\n{digitadas}')
            continue

        for i in range(0, len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                digitadas[i] = letra

        acertou = True
        for x in range(0, len(digitadas)):
            if digitadas[x] == '_':
                acertou = False

        if letra not in palavra_secreta:
            tentativas -= 1
            print(f'A letra "{letra}" NÃO existe.')

        if digitadas == palavra_secreta:
            print(f'\nVOCÊ GANHOU, POIS A PALAVRA SECRETA É:\n{digitadas}\n')
            break
        else:
            print(f'\n|    DESCUBRA A PALAVRA SECRETA    |\n{digitadas}')
