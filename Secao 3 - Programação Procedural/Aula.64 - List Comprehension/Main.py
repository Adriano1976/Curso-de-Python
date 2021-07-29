l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [var for var in l1]
print(ex1)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex2 = [var * 2 for var in l1]
print(ex2)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex3 = [(var1, var2) for var1 in l1 for var2 in range(3)]
print(ex3)

l4 = ['Luiz', 'Mauro', 'Maria', 'Adriano', 'Neide', 'Laura']
ex4 = [var.replace('a', '@').upper() for var in l4]
print(ex4)

tuple = (('chave1', 'valor1'), ('chave2', 'valor2'), ('chave3', 'valor3'), ('chave4', 'valor4'))
ex5 = [(y, x) for x, y in tuple]
print(ex5)

l5 = list(range(100))
ex6 = [var for var in l5 if var % 5 == 0]
print(ex6)

l6 = list(range(100))
ex7 = [var if var % 5 == 0 else '-' for var in l6]
print(ex7)

string = 'Mariana'

print(string[0:2], end='-')
print(string[2:4], end='-')
print(string[4:6], end='-')
print(string[6:8])

cpf = '90582226910'


def fatiador_cpf(string):
    temp = [string[i: i + 3] for i in range(0, 9, 3)]
    base = '.'.join(temp)
    digito = string[- (len(string) % 3):]
    return base + '-' + digito


print(fatiador_cpf(cpf))
