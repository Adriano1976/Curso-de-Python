'''
A classe Cliente é "dona" da classe Endereco, pois se cliente deixa de existir, endereço também deixa.
Portanto, na composição, a "classe endereço" é instanciada dentro da outra classe...
Com isso, você não tem acesso ao endereço fora da classe onde ela foi criada...
Além disso, quando você apagar a classe que criou o Endereço, o endereço também será apagado.
'''

from Classes import Cliente

cliente1 = Cliente('Adriano', 'Santos', 45)
cliente1.inserir_endereco('Luiz Algunsto Barreto', 85, 'Brisa Mar', 'Aruana', 'Aracaju', 'Sergipe', '49000510')

print(f'\nCódigo: {cliente1.cod}\nCliente: {cliente1.nome} {cliente1.sobrenome}')
print(f'Idade: {cliente1.idade} anos')
cliente1.listar_endereco()
