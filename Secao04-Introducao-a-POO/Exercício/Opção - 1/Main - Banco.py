"""
- Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo.
- Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco.
- A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta.
- Conta corrente tem um limite extra.
- Banco tem clientes e contas.

DICAS:

1 - Criar classe Cliente que herda da classe Pessoa (Herança).
    * Pessao tem nome e idade (com getters).
    * Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança).

2 - Criar classes ContaPoupança e ContaCorrente que herdem de Conta.
    * ContaCorrente deve ter um limite extra.
    * Contas devem ter método para depósito.
    * Conta (super classe) deve ter o método sacar abstrata (Abstração e Polimorfismo - as subclasses
    que implementam o método sacar).

3 - Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação).

4 - Banco será responsável em autenticar o cliente e as contas da seguintes maneira:
    * Banco tem contas e clientes (Agregação).
    * Checar se a agência é daquele banco.
    * Checar se o cliente é daquele banco.
    * Checar se a conta é daquele banco.

5 - Só será possivel sacar se passar na autenticação do banco (descrita acima)
"""

if __name__ == '__main__':
    from Banco import Banco, CC, CP, Cliente

    banco = Banco()
    conta1 = CC(4136, 111111, 1000)
    c1 = Cliente('Lucas', 17, conta1)
    banco.add_cliente(c1)
    c1.conta.sacar(500)
    print(c1.nome)
    print(c1.conta.saldo)

    print()

    conta2 = CP(4136, 213333, 300)
    c2 = Cliente('João', 32, conta2)
    banco.add_cliente(c2)
    c2.conta.sacar(200)
    print(c2.nome)
    print(c2.conta.saldo)
