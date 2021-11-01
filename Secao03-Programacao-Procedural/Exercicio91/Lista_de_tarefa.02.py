def mostrar_lista(funcao):
    for valores in funcao:
        print(f'\033[1;32m - {valores}')


def adicionar_tarefa():
    txt = input('\033[mDigite o item que deseja adicionar a lista: ').strip().title()
    lista.append(txt)
    return lista


def desfazer(lista):
    temporario.append(lista[-1])
    lista.pop()
    return lista


lista = []
temporario = []
while True:
    print('\033[1m- MENU DE OPÇÕES -')
    print('\033[m1 - Adicionar Item\n'
          '2 - Mostrar Itens\n'
          '3 - Desfazer\n'
          '4 - Refazer\n'
          '5 - Sair / Gerar Lista')
    while True:
        while True:
            try:
                acao = input('\033[1;33mDigite uma das opções acima: \033[m')
                acao = int(acao)
                break
            except:
                print('Digite apenas números')
                pass

        if acao > 5:
            print('O número digitado não corresponde a nehuma opção.')
        elif acao < 1:
            print('O número digitado não corresponde a nehuma opção.')
        else:
            break

    if acao == 1:
        adicionar_tarefa()
    elif acao == 2:
        print(f'\033[m{" "}', end='')
        print('\033[1m-=' * 20)
        print(f'\033[1;32m {"<<< LISTA >>>":^40}')
        mostrar_lista(lista)
        print(f'\033[m{" "}', end='')
        print('\033[1m-=' * 20)
    elif acao == 3:
        try:
            desfazer(lista)
        except:
            print('\033[1;31mNão há itens para desfazer'
                  '\nPor favor digite novamente!\033[m')
            pass
    elif acao == 4:
        try:
            lista.append(temporario[len(temporario) - 1])
            temporario.pop()
        except:
            print('\033[1;31mNão há itens para refazer'
                  '\nPor favor digite novamente!\033[m')
            pass
    elif acao == 5:
        nome = input('Digite o nome do arquivo para gerar sua lista (max 5 caracteres): ')[:6]
        nome += '.txt'
        titulo = input('Digite um título para sua lista:').upper()
        break

with open(nome, 'a+') as file:
    file.write(f'{titulo}\n')
    for itens in lista:
        file.write(f'{itens}\n')
    file.close()
print('Obrigado por consultar a lista!')
