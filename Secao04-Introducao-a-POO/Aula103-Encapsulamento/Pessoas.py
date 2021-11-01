class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    @property  # Obtem um valor
    def nome(self):
        # Você estava tentando obter um atributo privado
        # por fora da classe, se essa era realmente a intenção
        # então essa property resolve o problema
        return self.__nome


class Livro:
    def __init__(self, titulo, autor, tot_paginas, leitor):
        self.__titulo = titulo
        self.__autor = autor
        self.__tot_paginas = tot_paginas
        self.__pag_atual = 0
        self.__aberto = False

        # Aqui faz passar pelo setter
        self.leitor = leitor

    @property
    def leitor(self):
        return self.__leitor

    @leitor.setter  # Configura um valor.
    def leitor(self, valor):
        # Você não tinha o atributo nome em Pessoa
        # Então criei uma @property já que você criou
        # um atributo "privado" para __nome
        self.__leitor = valor.nome

    def detalhes(self):
        print(f'Leitor: {self.__leitor}\nTitulo: {self.__titulo}')
        pass


# main:
if __name__ == '__main__':
    p1 = Pessoa('Werberty', 22, 'M')
    l1 = Livro('Colecionador', 'Algust', 200, p1)
    l1.detalhes()  # Saída: Leitor=Werberty, Titulo=Colecionador
