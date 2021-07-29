from time import time

print()
def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\n\n\tA função "{funcao.__name__}"'
              f' levou {tempo:.2f}ms para executar')
        return resultado

    return interna


@velocidade
def demora():
    for i in range(1000):
        print(i, end='')


demora()