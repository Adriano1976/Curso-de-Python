from Buscador import buscador


while True:
    print('----------------------------------------------------------------------------------')
    print('--------------------------     Buscador de Arquivo     ---------------------------')
    print('----------------------------------------------------------------------------------')
    caminho = input('Digite um caminho: ')
    termo = input('Digite um termo: ')
    buscador(caminho, termo)

    print('\nDeseja continuar? [S/N]')
    opcao = input('Sair: ').upper()

    if opcao == 'S':
        continue
    else:
        break
