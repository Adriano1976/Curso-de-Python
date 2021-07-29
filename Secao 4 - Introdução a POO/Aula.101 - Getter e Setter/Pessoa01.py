class Pessoa:
    def __init__(self):
        self._nome = 'VALOR INICIAL'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor_que_vai_vir_do_sinal_de_igual):
        self._nome = valor_que_vai_vir_do_sinal_de_igual


pessoa = Pessoa()

# Quando chamo pessoa.nome estou executando o método nome()
# que está decorado com a property

print(pessoa.nome)  # 'VALOR INICIAL'

# Quando eu uso o sinal de atribuição (=) estou chamando o método
# nome.setter e passando o valor que vem depois do sinal de igual
# como argumento em valor_que_vai_vir_do_sinal_de_igual
# Veja:

pessoa.nome = 'VAI PASSAR PELO SETTER'
print(pessoa.nome)  # 'VAI PASSAR PELO SETTER'

# De novo

pessoa.nome = 'Luiz'
print(pessoa.nome)  # Luiz
