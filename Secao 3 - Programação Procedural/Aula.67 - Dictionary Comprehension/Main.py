lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]

d1 = {x: y.upper() for x, y in lista}
print(f'\nDicionário: {d1} do tipo {type(d1)}.')

d2 = {x for x in range(5)}
print(f'Set: {d2} do tipo {type(d2)}.')

d3 = {f'chave_{x}': x ** 2 for x in range(5)}
print(f'Dicionário: {d3} do tipo {type(d3)}.')
