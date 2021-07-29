class Carro:
    portas = 2

    def __init__(self):
        print('Carro criado')

    def definePortas(self, num):
        self.portas = num

    def exibePortas(self):
        return self.portas


if __name__ == '__main__':
    carro = Carro()
    num = int(input('Numero de portas: '))

    carro.definePortas(num)
    print('Numero de portas: ', carro.exibePortas())