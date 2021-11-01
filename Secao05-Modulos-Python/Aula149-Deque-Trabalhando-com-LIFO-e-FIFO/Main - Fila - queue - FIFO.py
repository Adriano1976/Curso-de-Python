"""
- Pilhas e filas.
- Pilhas (stack) - LIFO - last in, first out - Exemplo: Pilha de livros que são adicionados um sobre
o outro.
- Fila (queue) - FIFO - first in, first out - Exemplo: Uma fila de banco ou quelquer fila da vida real.
- As filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
- "append()" - Serve para colocar o objeto na fila.
- "popleft()" - Serve para retirar o objeto da fila seguindo a ordem de entrada.
"""
from collections import deque

fila = deque()
fila.append('João Pedro')
fila.append('Osvaldo Costa')
fila.append('Neide Ferreira')
fila.append('Adriano Santos')
fila.append('Sergio Fonseca')
fila.append('Maria Ferreira')

print()
for nome in fila:
    print(f'{nome} entrou na fila.')

print()
print(f'{fila.popleft()} saio da fila')
print(f'{fila.popleft()} saio da fila')
print(f'{fila.popleft()} saio da fila')
print(f'{fila.popleft()} saio da fila')
print(f'{fila.popleft()} saio da fila')

print()
for nome in fila:
    print(f'{nome} ainda está na fila.')
