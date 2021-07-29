from Pessoa import Pessoa

p1 = Pessoa('Adriano', 54)  # Usando o método de estância.

print(f'\n{p1.nome} está com a idade de {p1.idade} anos.')
print(f'{p1.nome} nasceu no ano de {p1.get_ano_nascimento()}.')  # Usando o método de classe.

print('-=' * 30)  #------------------------------------------------------------------------------

p2 = Pessoa.por_ano_nascimento('Neide', 1967)   # Usando o método de classe e imprimindo na tela.

print(f'{p2._nome} está com a idade de {p2.idade} anos.')
print(f'{p2._nome} nasceu no ano de {p2.get_ano_nascimento()}.')

print('-=' * 30)  #------------------------------------------------------------------------------

print(p1.get_data_atual())
print(p1.get_hora_atual())


