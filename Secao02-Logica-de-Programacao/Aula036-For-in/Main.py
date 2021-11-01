""" For in em Curso-de-Python Iterando strings com for. Função range (star=o, stop, step=1) """
for n in range(0, 100, 8):
    print(n)

print('\n##############\n')

for n in range(100):
    if n % 8 == 0:
        print(n)

print('\n##############\n')

texto = 'o rato roeu a ropa do reu de roma.'
print(texto)
nova_string = ''

for letra in texto:
    if letra == 'r':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)