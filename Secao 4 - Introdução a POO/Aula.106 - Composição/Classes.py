'''
A classe Cliente é "dona" da classe Endereco, pois se cliente deixa de existir, endereço também deixa.
Portanto, na composição, a "classe endereço" é instanciada dentro da outra classe...
Com isso, você não tem acesso ao endereço fora da classe onde ela foi criada...
Além disso, quando você apagar a classe que criou o Endereço, o endereço também será apagado.
'''

from random import randint


class Cliente:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.enderecos = []
        self.cod = randint(10000, 99999)

    def inserir_endereco(self, rua, numero, conjunto, bairro, cidade, estado, cep):
        self.enderecos.append(Endereco(rua, numero, conjunto, bairro, cidade, estado, cep))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(f'Rua: {endereco.rua}\n'
                  f'Número: {endereco._numero}\n'
                  f'Conjunto: {endereco.conjunto}\n'
                  f'Bairro: {endereco.bairro}\n'
                  f'Cidade: {endereco.cidade}\n'
                  f'Estado: {endereco.estado}\n'
                  f'CEP: {endereco.cep[:5]}-{endereco.cep[5:8]}')


class Endereco:
    def __init__(self, rua, numero, conjunto, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.conjunto = conjunto
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
