from Conta import Conta, Cliente

cliente_A = Cliente('Adriano', 'Santos', '234.896.147-49')
conta_A = Conta('00012300-4', cliente_A, 200.0, 1000.0)

cliente_N = Cliente('Neide Ferreira', 'Santos', '254.650.005-68')
conta_N = Conta('00054106-5', cliente_N, 300.0, 1000.0)

cliente_L = Cliente('Laura Beatriz Ferreira', 'Santos', '894.239.765-49')
conta_L = Conta('00032005-8', cliente_L, 500.0, 3000.0)

conta_A.extrato()
conta_A.deposita(200.0)
conta_A.extrato()
conta_A.saca(50)
conta_A.extrato()
conta_A.deposita(150)
conta_A.extrato()

conta_N.extrato()
conta_N.deposita(100)
conta_N.extrato()
conta_N.transfere_para(conta_A, 500)
conta_N.extrato()
conta_N.transfere_para(conta_A, 200)

print(f'\nTitular da conta {conta_A.numero}: {conta_A.titular.nome} {conta_A.titular.sobrenome}')
print(f'Titular da Conta {conta_N.numero}: {conta_N.titular.nome} {conta_N.titular.sobrenome}')
print(f'Titular da Conta {conta_L.numero}: {conta_L.titular.nome} {conta_N.titular.sobrenome}')

print(f'\nConta: {conta_A.numero}\n'
      f'Titular: {conta_A.titular.nome} {conta_A.titular.sobrenome}\n'
      f'Saldo: {conta_A.saldo}\n'
      f'Limite: {conta_A.limite}')

print(f'\nConta: {conta_N.numero}\n'
      f'Titular: {conta_N.titular.nome} {conta_N.titular.sobrenome}\n'
      f'Saldo: {conta_N.saldo}\n'
      f'Limite: {conta_N.limite}')

print(f'\nConta: {conta_L.numero}\n'
      f'Cliente: {cliente_L.nome} {cliente_L.sobrenome}\n'
      f'CPF: {cliente_L.cpf}\n'
      f'Saldo: {conta_L.saldo}\n'
      f'Limite: {conta_L.limite}')

print(f'\nReferência contaA do objeto: {id(conta_A)}')
print(f'Referência contaN do objeto: {id(conta_N)}')
print(f'Referência contaL do objeto: {id(conta_L)}')
