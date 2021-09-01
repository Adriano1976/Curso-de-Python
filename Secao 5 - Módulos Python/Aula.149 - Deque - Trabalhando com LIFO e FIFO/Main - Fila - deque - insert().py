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

fila.extend([1, 2, 3, 4, 5, 6, 7, 8])
print(fila)

fila.insert(2, 'Adriano Santos')
print(fila)
