"""
Lista em Python / fatiamento / append, insert, pop, del, clear, extend, min, max / range
"""
# índice: 0       1      2    3    4   5   6     7
lista = ['A', 'Banana', 'C', 'D', 'E', 5, 10.5, True]
print(lista)
print(lista[4])
print(lista[4:7])
print('----------------------')
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)
del (l2[3:5])
print(l2)
l2 = list(range(1, 20))
print(l2)
print('')

l5 = ['String', True, 10, -20.55]
for elem in l5:
    print(f' O tipo de elem é {type(elem)} e seu valor é {elem}.')