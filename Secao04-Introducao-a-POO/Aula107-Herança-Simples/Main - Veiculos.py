from Veiculo import Carro, Moto

if __name__ == '__main__':
    palio = Carro('carro', 'Palio Wind', '10.000', 'azul', 2)
    honda = Moto('moto', 'Honda', '5.000', 'amarelo', 4)

    print()
    palio.exibe()
    honda.exibe()
