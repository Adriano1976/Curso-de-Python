from Banco import ContaCorrente, Cliente, ContaPoupanca, Banco

cc = ContaCorrente(1111, 500600700, 50000, 1000)
cliente1 = Cliente("Paulo", 50, cc)

cp = ContaPoupanca(4444, 999999, 100000)
cliente2 = Cliente("Maria", 45, cp)

b = Banco()
b.novo_cadastro(cliente1)
b.novo_cadastro(cliente2)

if b.autenticar(cliente1):
    cliente1.consultar_saldo()
else:
    print("Autenticacao invalida!")

if b.autenticar(cliente2):
    cliente2.consultar_saldo()
else:
    print("Autenticacao invalida!")
