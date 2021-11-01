import random


class CaraCoroa:
    def __init__(self):
        self.lado = 'Cara'

    def lancar(self):
        if random.randint(0, 1) % 2 == 0:
            self.lado = 'Cara'.upper()
            return self.lado
        else:
            self.lado = 'Coroa'.upper()
            return self.lado


class Dado:
    def __init__(self):
        self.lado = 1

    def lancar(self):
        return random.randint(1, 6)


if __name__ == '__main__':
    moeda = CaraCoroa()
    dado = Dado()
    op = 1

    while op:
        print()
        op = int(input('0. Sair\n1. Lançar Moeda\n2. Lançar Dado\nOpção: '))

        if op == 1:
            print(moeda.lancar())
        elif op == 2:
            print(dado.lancar())
        else:
            print('Saindo do jogo...')
