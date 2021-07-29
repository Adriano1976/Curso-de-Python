'''
- No Python, o comportamento dos operadores é difinido por métodos especiais.
- Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''


class Retangulo:
    def __init__(self, x, y):  # construtor da classe...
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):  # Método de retornar um determinado  valor ou string...
        return f'<class "Retangulo {self.x}, {self.y}"'

    def __add__(self, other):  # Método de adição...
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):  # Método de comparação  do menor que...
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):  # Método de comparação maior que...
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):  # Método de comparação iqual a...
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


if __name__ == '__main__':
    r1 = Retangulo(10, 20)
    r2 = Retangulo(10, 20)
    print(r1 + r2)
    print(r2 < r1)
    print(r2 > r1)
    print(r1 == r2)
