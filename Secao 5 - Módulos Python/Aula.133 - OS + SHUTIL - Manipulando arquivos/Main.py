"""
- If you go to the file and press ctrl + l, it shows the full path.
- For those who work with the windows operating system, put the letter 'r' before a 'string'
to not have problems with the bars invested from windows itself when showing the file path.
"""
from Apagar import apagar
from Buscar import buscador
from Copiar import copiar
from Except import authenticNum, authenticString
from Mover import mover

while True:
    print()
    print('----------------------------------------------------------------------------------')
    print('---------------------------    MANIPULANDO ARQUIVOS    ---------------------------')
    print('----------------------------------------------------------------------------------')
    print('Informe a opção desejada:'.upper())
    print('\t1 - Pesquisar\n\t2 - Copiar\n\t3 - Mover\n\t4 - Apagar\n\t5 - Sair')
    opcao = authenticNum(input('Opção: '))
    if opcao is None:
        pass
    elif opcao == 1:
        while True:
            caminho = input('\nDigitar Caminho: ')
            termo = input('Digitar Termo: ')
            buscador(caminho, termo)

            print('\nDeseja continuar? [S/N]')
            opcao = authenticString(input('Opção: ').upper())
            if opcao == 'S':
                continue
            if opcao == 'N':
                break

    elif opcao == 2:
        while True:
            caminho_original = input('\nCaminho Original: ')
            caminho_novo = input('Caminho Desejado: ')
            copiar(caminho_original, caminho_novo)

            print('\nDeseja continuar? [S/N]')
            opcao = authenticString(input('Opção: ').upper())
            if opcao == 'S':
                continue
            if opcao == 'N':
                break

    elif opcao == 3:
        while True:
            caminho_original = input('\nCaminho Original: ')
            caminho_novo = input('Caminho Desejado: ')
            mover(caminho_original, caminho_novo)

            print('\nDeseja continuar? [S/N]')
            opcao = authenticString(input('Opção: ').upper())
            if opcao == 'S':
                continue
            if opcao == 'N':
                break

    elif opcao == 4:
        while True:
            caminho = input('\nCaminho Desejada: ')
            apagar(caminho)

            print('\nDeseja continuar? [S/N]')
            opcao = authenticString(input('Opção: ').upper())
            if opcao == 'S':
                continue
            if opcao == 'N':
                break
    else:
        print('\nsaindo do programa...')
        break
