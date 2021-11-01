file = open('abc.txt', 'w+')

file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('\nLendo linhas:')

print('---------------')

print(file.read(), end='')

print('---------------')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('---------------')

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

print('---------------')

# Forma geralmente usada para trabalhar com arquivo:
try:
    file = open('arquivo.txt', 'w+')
    file.write('Linha 101\n')
    file.write('Linha 102\n')
    file.write('Linha 103')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('---------------')

# Melhor forma de trabalhar com arquivo:
with open('arquivos.txt', 'w+') as file:
    file.write('linha 01\n')
    file.write('Linha 02\n')
    file.write('Linha 03\n')

    file.seek(0)
    print(file.read())

print('---------------')

# Melhor forma de trabalhar com arquivo:
with open('arquivos.txt', 'r') as file:
    print(file.read())

print('---------------')

with open('arquivos.txt', 'a+') as file:
    file.write('Outra linha')
    file.seek(0)
    print(file.read())

file.close()
