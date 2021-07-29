class Cliente:
    def __init__(self, cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self.numcpf

    @cpf.setter
    def cpf(self, valor):
        valor = str(valor)
        valor = f'{valor[:3]}.{valor[3:6]}.{valor[6:9]}-{valor[9:]}'
        self.numcpf = valor


if __name__ == "__main__":
    resp = 0
    while True:
            cliente = Cliente(input('\nDegite o número do CPF: '))
            print(cliente.cpf)
            resp = input('Deseja continuar? [S/N]: ').title()
            if resp == 'S':
                continue
            else:
                break
