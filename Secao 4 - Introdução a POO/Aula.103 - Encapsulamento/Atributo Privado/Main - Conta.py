from Conta import Cliente, Conta

cliente_A = Cliente('Adriano', 'Santos', '234.896.147-49')
conta_A = Conta('00010023-4', cliente_A, 200.0, 1000.0)

cliente_N = Cliente('Neide Ferreira', 'Santos', '254.650.005-68')
conta_N = Conta('00005416-5', cliente_N, 300.0, 1000.0)

cliente_L = Cliente('Laura Beatriz Ferreira', 'Santos', '894.239.765-49')
conta_L = Conta('00032005-8', cliente_L, 500.0, 3000.0)

print()
print(f'Titular da conta {conta_A.numero}: {conta_A.titular.nome} {conta_A.titular.sobrenome}')
print(f'Titular da Conta {conta_N.numero}: {conta_N.titular.nome} {conta_N.titular.sobrenome}')
print(f'Titular da Conta {conta_L.numero}: {conta_L.titular.nome} {conta_N.titular.sobrenome}')

conta_A.extrato()
conta_A.deposita(200.0)
conta_A.extrato()
conta_A.saca(50)
conta_A.extrato()
conta_A.deposita(150)
conta_A.extrato()
conta_A.transfere_para(conta_L, 50)
conta_A.historico.imprime()  # ----------------------------------------------------------------

conta_N.extrato()
conta_N.deposita(100)
conta_N.extrato()
conta_N.transfere_para(conta_A, 500)
conta_N.extrato()
conta_N.transfere_para(conta_A, 200)
conta_N.historico.imprime()  # ----------------------------------------------------------------

conta_L.extrato()
conta_L.deposita(80)
conta_L.extrato()
conta_L.deposita(15)
conta_L.extrato()
conta_L.deposita(150)
conta_L.extrato()
conta_L.saca(50)
conta_L.extrato()
conta_L.historico.imprime()  # ----------------------------------------------------------------

print('-------------------------------------------')
print('|        DADOS DA CONTA DO CLIENTE        |')
print('-------------------------------------------')
print(f'\tConta: {conta_A.numero}\n'
      f'\tTitular: {conta_A.titular.nome} {conta_A.titular.sobrenome}\n'
      f'\tSaldo: {conta_A.saldo}\n'
      f'\tLimite: {conta_A.limite}\n'
      f'------- {conta_A.historico.data_abertura} --------\n')

print('-------------------------------------------')
print('|        DADOS DA CONTA DO CLIENTE        |')
print('-------------------------------------------')
print(f'\tConta: {conta_N.numero}\n'
      f'\tTitular: {conta_N.titular.nome} {conta_N.titular.sobrenome}\n'
      f'\tSaldo: {conta_N.saldo}\n'
      f'\tLimite: {conta_N.limite}\n'
      f'------- {conta_A.historico.data_abertura} --------\n')

print('-------------------------------------------')
print('|        DADOS DA CONTA DO CLIENTE        |')
print('-------------------------------------------')
print(f'\tConta: {conta_L.numero}\n'
      f'\tCliente: {cliente_L.nome} {cliente_L.sobrenome}\n'
      f'\tCPF: {cliente_L.cpf}\n'
      f'\tSaldo: {conta_L.saldo}\n'
      f'\tLimite: {conta_L.limite}\n'
      f'------- {conta_A.historico.data_abertura} --------\n')

print(f'Referência contaA do objeto: {id(conta_A)}')
print(f'Referência contaN do objeto: {id(conta_N)}')
print(f'Referência contaL do objeto: {id(conta_L)}')

print()
for var in dir(conta_A):
    print(var)

"""
- Repare que o erro acusa que a classe Conta não possui o atributo __dict__. 
- Ao atribuir um valor para __slots__, o interpretador do Python vai entender que queremos excluir 
o __dict__ da classe Conta não sendo possível criar atributos, ou seja, impossibilitando adicionar 
atributos ao dicionário da classe que é responsável	por armazenar atributos	de instância.
"""

print()
print(conta_A.__dict__)
