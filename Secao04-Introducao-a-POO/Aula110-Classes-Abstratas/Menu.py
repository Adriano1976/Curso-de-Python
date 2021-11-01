import time

import Message
from Conta_corrente import ContaCorrente
from Conta_poupança import ContaPoupança


def menu():
    while True:
        Message.account_type()  # Informando o tipo de conta a ser criada ..............................................
        escolher_tipo_de_conta = int(input("Opção: "))
        print()

        if escolher_tipo_de_conta == 1:
            while True:
                Message.create_checking_account()  # Criação Conta Corrente ............................................
                tipo_cc = 'Conta Corrente'
                agencia_cc = int(input("\tAgência: "))
                conta_cc = input("\tConta: ")
                saldo_cc = float(input("\tSaldo: "))
                limite_cc = float(input("\tLimite: "))

                conta_corrente = ContaCorrente(tipo_cc, agencia_cc, conta_cc, saldo_cc, limite_cc)  # Conta Criada .....
                conta_corrente.detalhes()  # Imprimindo os detalhes da conta criada ....................................

                resp = input('Deseja continuar? [S/N]: ')
                if resp == 's' or resp == 'S':
                    while True:
                        Message.operate_checking_account()  # Imprimindo as opções de operação da conta corrente .......
                        escolher_cc = int(input("Opção: "))

                        if escolher_cc == 1:  # Opção depositar valor ..................................................
                            while True:
                                valor_dep_cc = float(input("\tValor: "))
                                conta_corrente.depositar(valor_dep_cc)
                                conta_corrente.detalhes()

                                resp = input('Deseja continuar? [S/N]: ')
                                if resp == 's' or resp == 'S':
                                    continue
                                if resp == 'n' or resp == 'N':
                                    break
                                pass

                        if escolher_cc == 2:  # Opção Sacar Valor ......................................................
                            while True:
                                valor_saque_cc = float(input("\tValor: "))
                                conta_corrente.sacar(valor_saque_cc)

                                resp = input('Deseja continuar? [S/N]: ')
                                if resp == 's' or resp == 'S':
                                    continue
                                if resp == 'n' or resp == 'N':
                                    break
                                pass

                        if escolher_cc == 3:  # Opção Visualizar Extrato da Conta ......................................
                            conta_corrente.detalhes()

                            resp = input('Deseja continuar? [S/N]: ')
                            if resp == 's' or resp == 'S':
                                continue
                            if resp == 'n' or resp == 'N':
                                break

                        if escolher_cc == 4:  # Opção Visualizar Histórico da Conta ....................................
                            pass

                            resp = input('Deseja continuar? [S/N]: ')
                            if resp == 's' or resp == 'S':
                                continue
                            if resp == 'n' or resp == 'N':
                                break
                            pass

                        if escolher_cc == 5:
                            break
                        break
                    menu()
                    break

                elif resp == 'n' or resp == 'N':
                    menu()
                    break

        if escolher_tipo_de_conta == 2:
            while True:
                Message.create_savings_account()  # Criaando Conta Poupança ............................................
                tipo_cp = 'Conta Poupança'
                agencia_cp = int(input("Agência: "))
                conta_cp = input("Conta: ")
                saldo_cp = float(input("Saldo: "))
                conta_poupanca = ContaPoupança(tipo_cp, agencia_cp, conta_cp, saldo_cp)
                conta_poupanca.detalhes()  # Imprimindo os detalhes da conta criada ....................................

                resp = input('Deseja continuar? [S/N]: ')
                if resp == 's' or resp == 'S':
                    while True:
                        Message.operate_savings_account()  # Operação da conta corrente ................................
                        escolher_cp = int(input("Opção: "))

                        if escolher_cp == 1:  # Depositar valor na conta corrente ......................................
                            while True:
                                valor_dep_cp = float(input("\tValor: "))
                                conta_poupanca.depositar(valor_dep_cp)

                                resp = input('Deseja continuar? [S/N]: ')
                                if resp == 's' or resp == 'S':
                                    continue
                                if resp == 'n' or resp == 'N':
                                    break
                                pass

                        if escolher_cp == 2:   # Opção Sacar Valor ....................................................
                            while True:
                                valor_saque_cp = float(input("\nValor: "))
                                conta_poupanca.sacar(valor_saque_cp)

                                resp = input('Deseja continuar? [S/N]: ')
                                if resp == 's' or resp == 'S':
                                    continue
                                if resp == 'n' or resp == 'N':
                                    break
                                pass

                        if escolher_cp == 3:
                            conta_poupanca.detalhes()  # Opção Visualizar Extrato da Conta .............................

                            resp = input('Deseja continuar? [S/N]: ')
                            if resp == 's' or resp == 'S':
                                continue
                            if resp == 'n' or resp == 'N':
                                break

                        if escolher_cp == 4:
                            pass

                            resp = input('Deseja continuar? [S/N]: ')
                            if resp == 's' or resp == 'S':
                                continue
                            if resp == 'n' or resp == 'N':
                                break

                        if escolher_cp == 5:
                            break
                        break
                    menu()
                    break

                elif resp == 'n' or resp == 'N':
                    menu()
                    break

        if escolher_tipo_de_conta == 3:
            print("Saindo...")
            time.sleep(1.5)
            break
        break


menu()
