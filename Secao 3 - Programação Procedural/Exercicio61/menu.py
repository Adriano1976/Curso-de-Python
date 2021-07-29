import VelhoTestamento
import NovoTestamento
import LivroDeMormon
import DoutrinaConvenios

def menu():

    print()
    print('---------------------------------------------------------------')
    print('---  MENU DO JOGOS DE PERGUNTAS E RESPOSTAS DAS ESCRITURAS  ---')
    print('---------------------------------------------------------------')
    print('-----------  1. O Velho Testamento  ---------------------------')
    print('-----------  2. O Novo Testamento  ----------------------------')
    print('-----------  3. O Livro de Mórmon  ----------------------------')
    print('-----------  4. Doutrina e Convêncios  ------------------------')
    print('-----------  5. Sair  -----------------------------------------')

    escolha = int(input('Escolha o tema das perguntas.\nDigite o número: '))

    if escolha == 1:
        VelhoTestamento.jogar()
    if escolha == 2:
        NovoTestamento.jogar()
    if escolha == 3:
        LivroDeMormon.jogar()
    if escolha == 4:
        DoutrinaConvenios.jogar()
    if escolha == 5:
        print('\nFinalizando jogo...')

menu()