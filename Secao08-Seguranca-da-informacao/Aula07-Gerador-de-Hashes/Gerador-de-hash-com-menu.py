import hashlib
from time import sleep

while True:
    print('--------- GERADOR DE HASH ---------')
    texto = input('Digite o Texto ou 1 - Sair: ')

    # Nessa opção, se o usuário digitou 1 ou click em enter, estará saindo do programa.
    if texto == '1' or texto == '<return>':
        print('Saindo do programa...')
        sleep(0.85)
        break

    # Se digitou o texto a ser gerado a hash, entrará no menu para escolher o tipo de hash.
    else:
        while True:
            menu = int(input('''Escolha o Tipo:
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            5) Sair
            Opção:  '''))
            print()

            # Nessa opção, será processado e gerado um hash do tipo md5.
            if menu == 1:
                print('Processando...')
                sleep(0.85)
                resultado = hashlib.md5(texto.encode('utf-8'))
                print(f'A hash MD5 do texto "{texto}": {resultado.hexdigest()}\n')

            # Nessa opção, será processado e gerado um hash do tipo sha1.
            elif menu == 2:
                print('Processando...')
                sleep(0.85)
                resultado = hashlib.sha1(texto.encode('utf-8'))
                print(f'A hash SHA1 do texto "{texto}": {resultado.hexdigest()}\n')

            # Nessa opção, será processado e gerado um hash do tipo cha256.
            elif menu == 3:
                print('Processando...')
                sleep(0.85)
                resultado = hashlib.sha256(texto.encode('utf-8'))
                print(f'A hash SHA256 do texto "{texto}": {resultado.hexdigest()}\n')

            # Nessa opção, será processado e gerado um hash do tipo sha512.
            elif menu == 4:
                print('Processando...')
                sleep(0.85)
                resultado = hashlib.sha512(texto.encode('utf-8'))
                print(f'A hash SHA512 do texto "{texto}": {resultado.hexdigest()}\n')

            # Nessa opção, será realizado a saida do usuário do programa.
            elif menu == 5:
                print('Saindo do programa...\n')
                sleep(0.85)
                break

            # Nessa opção, se o usuário digitar a oção errada ou click enter, será informado da invalidade.
            elif menu != int or menu == '<return>':
                print('Opção inválida. Tente novamente\n')
                continue

            # Nessa condição, o usuário está saindo do programa.
            else:
                print('Saindo do programa...')
                sleep(0.85)
                break
            break
