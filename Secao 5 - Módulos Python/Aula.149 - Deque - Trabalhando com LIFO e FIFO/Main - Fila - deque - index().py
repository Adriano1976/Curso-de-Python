"""
- Pilhas e filas.
- Pilhas (stack) - LIFO - last in, first out - Exemplo: Pilha de livros que são adicionados um sobre
o outro.
- Fila (queue) - FIFO - first in, first out - Exemplo: Uma fila de banco ou quelquer fila da vida real.
- As filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
"""
from collections import deque

fila = deque(maxlen=10)

fila.extend(
    [
        10,  # índice 0
        20,  # índice 1
        30,  # índice 2
        40,  # índice 3
        50,  # índice 4
        60,  # índice 5
        70,  # índice 6
        80   # índice 7
    ]
)
print()
print(f'Índice ou posição: {fila.index(20)}')
print(f'Índice ou posição: {fila.index(50)}')
print(f'Índice ou posição: {fila.index(80)}')
