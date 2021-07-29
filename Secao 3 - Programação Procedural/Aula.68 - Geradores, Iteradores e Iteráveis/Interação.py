import time


def gerar():
    lista = []
    for var in range(100):
        lista.append(var)
        time.sleep(0.1)
    return lista


g = gerar()
print(f'Tipo: {type(g)}')

for var in g:
    print(var)
