from time import sleep

conjListas = [
    [*range(1, 20), 5, 8, 7, 8],
    [*range(1, 20), 9, 2, 7, 5],
    [*range(10, 27), 1, 5, 8, 7],
    [*range(1, 20), 5, 7, 9, 4],
    [*range(8, 25), 4, 7, 4, 7],
    [*range(4, 22), 5, 8, 9, 6],
    [*range(9, 26), 4, 8, 10, 1],
    [*range(1, 20), 1, 3, 5, 8],
]

print()
for lista in conjListas:

    contador = 0

    if (len(set(lista)) < len(lista)):
        for numero in set(lista):
            if lista.count(numero) > 1:
                contador += 1
        print(lista, f"------->>> [ {contador} ]")
        sleep(1.3)
    else:
        print(lista, "------->>> [ 0 ]")
        sleep(1.3)
