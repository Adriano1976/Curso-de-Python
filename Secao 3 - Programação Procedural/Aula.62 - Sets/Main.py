'''
- add (adiciona), update (atualiza), clear (apagar), discard (remover).
- union | (une).
- intersection & (todos os elementos presentes nos dois sets).
- difference - (elementos apenas no set da esquerda)
- symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
'''
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add((1, 2, 3, 'Adriano'))
print(s1)
s1.discard(2)
print(s1)
s1.update('Neide')
print(s1)
print()

l1 = [1, 1, 2, 2, 3, 3, 5, 4, 6, 8, 7, 9, 'Carlos', 'Laura']
print(f'Lista: {l1}')
l1 = set(l1)
print(f'Set: {l1}\n')

v1 = {1, 2, 3, 4, 5}
v2 = {1, 4, 5, 6, 7, 8, 9, 0, 11, 20}
v3 = v1 | v2
print(f'A união entre {v1} e {v2} resultou em {v3} sem repetição dos elementos.')

v4 = v1 & v2
print(f'A união entre {v1} e {v2} resultou em {v4} de todos os elementos presentes nos dois sets.')

v5 = v1 - v2
print(f'A união entre {v1} e {v2} resultou em {v5} dos elementos apenas no set da esquerda.')

v6 = v1 ^ v2
print(f'A união entre {v1} e {v2} resultou em {v6} do elementos que estão nos dois sets, mas não em ambos.')