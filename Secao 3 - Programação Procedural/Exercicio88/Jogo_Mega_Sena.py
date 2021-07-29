import random
import json

'''
- Gerador de jogos da Mega Sena.
- Banco de dados (arquivo) com os 20 últimos sorteios.
- Usuário pode substituir o sorteio mais antigo pelo atual.
- O programa gera aleatoriamente a quantidade de jogos determinada pelo usuário.
'''


def gerador_arquivo(lista_jogos):
    jogos1_json = json.dumps(lista_jogos, indent=True)
    with open('jogos.json', 'w+') as arquivo1:
        arquivo1.write(jogos1_json)
        arquivo1.seek(0)


def gerador_lista(jogos2_json):
    nova_lista = jogos2_json
    lista_variante = []
    while True:
        resp = input('Deseja substituir o sorteio mais antigo pelo atual? [S/N]: ').upper()[0].strip()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('ERRO! Digite apenas S ou N...')
    if resp == 'S':
        cont = 1
        while cont < 7:
            try:
                numeros = int(input(f'Digite a {cont}ª dezena: '))
                lista_variante.append(numeros)
                cont += 1
            except ValueError:
                print('ERRO! Digite apenas numeros inteiros')
            if len(lista_variante) == 6:
                break
        del nova_lista[0]
        nova_lista.append(lista_variante)
        return nova_lista
    else:
        return nova_lista


def gerador_jogos(lista_final):
    jogos = []
    jogos2 = []
    dezenas = []
    for var in lista_final:
        for d in var:
            dezenas.append(d)
    while True:
        try:
            quantidade = int(input('Deseja gerar quantos jogos?: '))
            for var in range(quantidade):
                contador = 1
                while contador < 7:
                    numero = random.choice(dezenas)
                    if not numero in jogos:
                        jogos.append(numero)
                        contador += 1
                jogos.sort()
                jogos2.append(jogos[:])
                jogos.clear()
            break
        except ValueError:
            print('ERRO! Digite apenas números inteiros...')
    return jogos2


print()
lista_jogos = [
    [7, 8, 14, 23, 30, 46], [9, 24, 33, 43, 49, 57], [2, 3, 8, 19, 29, 37], [14, 20, 23, 39, 46, 50],
    [10, 23, 31, 37, 58, 59], [20, 32, 33, 48, 49, 53], [4, 13, 23, 28, 30, 52], [1, 11, 14, 23, 29, 55],
    [14, 16, 38, 39, 41, 48], [6, 10, 27, 28, 41, 52], [2, 5, 11, 24, 41, 49], [15, 16, 20, 38, 40, 58],
    [8, 11, 17, 33, 40, 55], [2, 4, 25, 36, 50, 53], [5, 15, 18, 27, 49, 57], [10, 22, 23, 37, 53, 60],
    [8, 17, 34, 37, 43, 45], [5, 12, 14, 20, 27, 28], [28, 29, 31, 50, 58, 59], [14, 27, 35, 40, 50, 55],
]

try:
    with open('jogos.json', 'r+') as arquivo:
        jogos2_json = arquivo.read()
        jogos2_json = json.loads(jogos2_json)
        lista_final = gerador_lista(jogos2_json)
        print()
        lista_final2 = gerador_jogos(lista_final)
    jogos_json = json.dumps(lista_final, indent=True)

    with open('jogos.json', 'w+') as arquivo3:
        arquivo3.write(jogos_json)
        arquivo3.seek(0)
except FileNotFoundError:
    gerador_arquivo(lista_jogos)

    with open('jogos.json', 'r+') as arquivo:
        jogos2_json = arquivo.read()
        jogos2_json = json.loads(jogos2_json)
        lista_final = gerador_lista(jogos2_json)
        print()
        lista_final2 = gerador_jogos(lista_final)
    jogos_json = json.dumps(lista_final, indent=True)

    with open('jogos.json', 'w+') as arquivo3:
        arquivo3.write(jogos_json)
        arquivo3.seek(0)

print()
print('Lista Atualizada:')
for cont1 in range(len(lista_final)):
    print(f'\t{cont1 + 1:3}° Jogo: {lista_final[cont1]}')

print()
print('-' * 42)
print(f'# {len(lista_final2)} Jogos Gerados com Sucesso!!!')
print()
for cont2 in range(len(lista_final2)):
    print(f'\t{cont2 + 1:3}° Jogo: {lista_final2[cont2]}')
print('-' * 42)

print()
print('>>>>>>>>>>>>>>>> BOA SORTE <<<<<<<<<<<<<<<')
