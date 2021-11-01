"""
- Pilhas e filas.
- Pilhas (stack) - LIFO - last in, first out - Exemplo: Pilha de livros que são adicionados um sobre
o outro.
- Fila (queue) - FIFO - first in, first out - Exemplo: Uma fila de banco ou quelquer fila da vida real.
- As filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os índices
serão modificados.
"""
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

print(f'Lista de livros: {livros}')

livro_removido = livros.pop()

print(f'Lista de livros: {livros}')
print(f'\nLivro removido: {livro_removido}')

livro_removido = livros.pop()

print(f'Lista de livros: {livros}')
print(f'\nLivro removido: {livro_removido}')
