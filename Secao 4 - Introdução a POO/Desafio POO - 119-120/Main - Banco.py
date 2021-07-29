from Banco import Banco
from Contas import ContaCorrente, ContaPoupanca
from Cliente import Cliente

# Cadastro do cliente1 e criação da Conta Corrente do mesmo cliente.
cliente1 = Cliente('Adriano', 'Santos', 45, '458.587.159-45')
cc1 = ContaCorrente(cliente1, 2170, '2145800-5', 0)

# Cadastro do cliente2 e criação da Conta Poupança do mesmo criente.
cliente2 = Cliente('Neide Ferreira', 'Santos', 55, '458.759.005-45')
cp1 = ContaPoupanca(cliente2, 2070, '4124580-0', 0)

# O cadastro do cliente, juntamente com sua conta, são acrescentados no sistema do banco.
banco = Banco()
banco.acrescente(cliente1, cc1)
banco.acrescente(cliente2, cp1)

while True:

    string = ' MENU - TIPO DE CONTA '
    quant = len(string)

    print()
    print('-' * quant)
    print(string)
    print('-' * quant)
    print('\t1 - Conta Corrente')
    print('\t2 - Conta Poupança')
    print('\t0 - Sair')
    opcao = input('Opção: ')

    # Oção 1 - Tratativa referente a Conta Corrente do cliente
    if opcao == '1':
        cc1.detalhes()

        # A conta corrente inicializa o processo de autenticação apartir daqui
        while True:
            string = ' AUTENTICAÇÃO - CONTA CORRENTE '
            quant = len(string)

            print('-' * quant)
            print(string)
            print('-' * quant)
            print('\t1 - Autenticar\n'
                  '\t0 - Sair')

            opcao = input('Opção: ')

            if opcao == '1':
                # O banco irá autenticar o cliente, a agência e a conta se for desse banco.
                if banco.autentica(cliente1, cc1):
                    while True:
                        string = ' MENU - CONTA CORRENTE '
                        quant = len(string)

                        print('-' * quant)
                        print(string)
                        print('-' * quant)

                        print('\t1 - Depósito\n'
                              '\t2 - Saque\n'
                              '\t3 - Transferência\n'
                              '\t4 - Saldo\n'
                              '\t5 - Extrato\n'
                              '\t0 - Sair')

                        opcao = input('Opção: ')

                        if opcao == '1':
                            cc1.deposita(float(input('\tValor: ')))
                        elif opcao == '2':
                            cc1.sacar(float(input('\tValor: ')))
                        elif opcao == '3':
                            cc1.transfere(cp1, float(input('\tValor: ')))
                        elif opcao == '4':
                            cc1.detalhes()
                        elif opcao == '5':
                            cc1.extrato()
                        else:
                            break
                else:
                    cc1.detalhes()
            else:
                break

    # Opção 2 - Tratativa referente a Conta Poupança do cliente
    elif opcao == '2':
        cp1.detalhes()

        while True:
            string = ' AUTENTICAÇÃO - CONTA POUPANÇA '
            quant = len(string)

            print('-' * quant)
            print(string)
            print('-' * quant)

            print('\t1 - Autenticar\n'
                  '\t0 - Sair')

            opcao = input('Opção: ')

            if opcao == '1':
                # O banco irá autenticar o cliente, a agência e a conta se for desse banco.
                if banco.autentica(cliente2, cp1):
                    while True:
                        string = ' MENU - CONTA POUPANÇA '
                        quant = len(string)

                        print('-' * quant)
                        print(string)
                        print('-' * quant)

                        print('\t1 - Depósito\n'
                              '\t2 - Saque\n'
                              '\t3 - Transferência\n'
                              '\t4 - Saldo\n'
                              '\t5 - Extrato\n'
                              '\t0 - Sair')

                        opcao = input('Opção: ')

                        if opcao == '1':
                            cp1.deposita(float(input('\tValor: ')))
                        elif opcao == '2':
                            cp1.sacar(float(input('\tValor: ')))
                        elif opcao == '3':
                            cp1.transfere(cc1, float(input('\tValor: ')))
                        elif opcao == '4':
                            cp1.detalhes()
                        elif opcao == '5':
                            cp1.extrato()
                        else:
                            break
                else:
                    cp1.detalhes()
            else:
                break

    else:
        # Oção 0 - Sair do programa
        break
