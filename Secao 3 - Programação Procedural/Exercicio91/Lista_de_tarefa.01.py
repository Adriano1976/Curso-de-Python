from time import sleep

def mostrarTarefa(listaTarefa):
    print('\n----------------------------------------')
    print('----------- \033[1;33mLISTA DE TAREFAS\033[m -----------')
    print('----------------------------------------')
    for tarefa in listaTarefa:
        print('- ', tarefa)
    print('----------------------------------------')
    return

def opcaoTarefa():
    print('\n\033[1;33mDigite a Opção da Tarefa Desejada:\033[m')
    print('\t1 - Mostrar\n\t2 - Desfazer\n\t3 - Refazer\n\t4 - Adicionar\n\t5 - Criar Arquivo\n\t6 - sair')
    return

def opcaoContinuar():
    print('\nDedeja Continuar?\n1 - Sim\n2 - Não')
    return

def desfazerTarefa(listaTarefa, listaTemp):
    if not listaTarefa:
        print('\033[1;31mNada a Desfazer\033[m')
        return

    tarefa = listaTarefa.pop()
    listaTemp.append(tarefa)


def refazerTarefa(listaTarefa, listaTemp):
    if not listaTemp:
        print('\033[1;31mNada a Refazer\033[m')
        return

    tarefa = listaTemp.pop()
    listaTarefa.append(tarefa)


def adicionarTarefa(tarefa, listaTarefa):
    listaTarefa.append(tarefa)


def sair():
    print('\nFinalizando programa...')
    sleep(1.3)
    return


if __name__ == '__main__':
    listaTarefa = []
    listaTemp = []

    print('---------------------------------------')
    print('---------- \033[1;33mAGENDA DE TAREFAS\033[m ----------')
    print('---------------------------------------')

    while True:
        opcaoTarefa()
        while True:

            while True:

                try:
                    option = input('\033[1;33mOpção:\033[m ')
                    option = int(option)
                    break
                except:
                    print('\033[1;31mOpção Incorreta. Digite Apenas Números.\033[m')
                    opcaoTarefa()
                    pass

            if option > 6:
                print('\033[1;31mOpção de Tarefa Incorreta.\033[m')
                opcaoTarefa()
            elif option < 1:
                print('\033[1;31mOpção de Tarefa Incorreta.\033[m')
                opcaoTarefa()
            else:
                break

        if option == 1:
            mostrarTarefa(listaTarefa)
            continue
        elif option == 2:
            desfazerTarefa(listaTarefa, listaTemp)
            continue
        elif option == 3:
            refazerTarefa(listaTarefa, listaTemp)
            continue
        elif option == 4:
            while True:
                tarefa = input('\n\033[1mDigite a Tarefa: ').capitalize()
                adicionarTarefa(tarefa, listaTarefa)
                opcaoContinuar()

                while True:
                    while True:

                        try:
                            opcao = input('\033[1;33mOpção:\033[m ')
                            opcao = int(opcao)
                            break
                        except:
                            print('\033[1;31mOpção Incorreta. Digite Apenas Números.\033[m\n')
                            opcaoContinuar()
                            pass

                    if opcao < 1:
                        print('\033[1;31mOpção de Tarefa Incorreta.\033[m\n')
                        opcaoContinuar()
                    elif opcao > 2:
                        print('\033[1;31mOpção de Tarefa Incorreta.\033[m\n')
                        opcaoContinuar()
                    else:
                        break

                if opcao == 1:
                    continue
                elif opcao == 2:
                    break
            continue

        elif option == 5:
            nome = input('\nDigite o Nome do Arquivo: ').capitalize()
            nome += '.txt'
            titulo = input('Digite o Título da Tarefa: ').upper()

            with open(nome, 'a+') as file:
                file.write(f'---------- {titulo} ----------\n')
                for itens in listaTarefa:
                    file.write(f'\t- {itens}\n')
                file.seek(0, 0)
                print('\n\033[1;33mCriar Arquivo...\n\033[m')
                sleep(1.3)
                print(file.read())
                file.close()
            continue
        else:
            option == 6
            sair()
            break
