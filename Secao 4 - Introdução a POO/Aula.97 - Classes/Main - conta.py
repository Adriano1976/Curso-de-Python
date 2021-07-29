from conta import Conta, Cliente

conta = Conta('000123-04', 'Adriano Santos', 120.0, 1000.0)
contaVIP = Conta('000514-45', 'Neide Ferreira', 300.55, 525.75)

titular = Cliente('Adriano', 'Santos', '894.651.236-25')
titularVIP = Cliente('Neide', 'Ferreira', '568.254.005.68')


print()
print('--------------------------------')
print('|  CRIAÇÃO DA CONTA DO CLIENTE  |')
print('--------------------------------')
print(f'Cliente: {titular.nome} {titular.sobrenome}')
print(f'CPF: {titular.cpf}')
print(f'Nª Conta: {conta.numero}')
print(f'Saldo: {conta.saldo}')
print(f'Limite: {conta.limite}')
print(f'Data: {conta.data}')
print('Imprimindo...')

titular.imprimir()
conta.historico.imprime()

contaVIP.depositar(350)
conta.depositar(260)
conta.sacar(80)
contaVIP.depositar(650)
contaVIP.sacar(50)
contaVIP.trasnferir_para(conta, 50)
conta.trasnferir_para(contaVIP, 150.75)
conta.historico.imprime()
contaVIP.historico.imprime()