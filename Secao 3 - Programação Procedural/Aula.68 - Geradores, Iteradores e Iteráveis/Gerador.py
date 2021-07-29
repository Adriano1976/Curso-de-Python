import time


def gerador():
    for var in range(100):
        yield var
        time.sleep(0.1)


g = gerador()
print(f'Tipo: {type(g)}')

for var in g:
    print(var)
