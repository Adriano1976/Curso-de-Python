"""
- Pilhas e filas.
- Pilhas (stack) - LIFO - last in, first out - Exemplo: Pilha de livros que são adicionados um sobre
o outro.
- Fila (queue) - FIFO - first in, first out - Exemplo: Uma fila de banco ou quelquer fila da vida real.
- As filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
- "popleft()" - Serve para retirar o objeto da fila seguindo a ordem de entrada.
"""
from _collections import deque

livros = deque()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

print(f'\nLista de livros: {livros}')
print(f'\nSaiu o {livros.popleft()}')

nome_livro = livros.popleft()

while livros:
    print(f'Saiu o {nome_livro}')
    nome_livro = livros.popleft()

print(f'\nFicou o {nome_livro}')
