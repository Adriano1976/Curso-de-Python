"""
- Pilhas e filas.
- Pilhas (stack) - LIFO - last in, first out - Exemplo: Pilha de livros que são adicionados um sobre
o outro.
- Fila (queue) - FIFO - first in, first out - Exemplo: Uma fila de banco ou quelquer fila da vida real.
- As filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
- "reverse" - Serve para inverter a posição de todos os objetos de uma fila.
"""
from collections import deque

fila = deque(maxlen=10)

print()
fila.extend([10, 20, 30, 40, 50, 60, 70, 80])
print(f'Fila normal:    {fila}')
fila.reverse()
print(f'Fila invertida: {fila}')
