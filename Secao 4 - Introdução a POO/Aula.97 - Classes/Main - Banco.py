from Banco import Conta

if __name__ == '__main__':
    pessoa = Conta()

    op = True
    while op:
        print()
        print('0. Sair')
        print('1. Exibir saldo')
        print('2. Depositar')
        print('3. Sacar')
        op = int(input('Opção: '))

        if op == 1:
            print(f'Saldo: {pessoa.exibeSaldo()}')
        elif op == 2:
            num = float(input('Valor para depositar: '))
            pessoa.depositar(num)
        elif op == 3:
            num = float(input('Valor para sacar: '))
            pessoa.sacar(num)
        else:
            print('Saindo do sistema...')
