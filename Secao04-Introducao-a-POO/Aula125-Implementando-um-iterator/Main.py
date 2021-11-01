class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):  # Get the values in brackets.
        return self.__items[index]

    def __setitem__(self, index, value):  # Serves to set the values in square brackets.
        if index >= len(self.__items):
            self.__items.append(value)
        self.__items[index] = value

    def __delitem__(self, index):  # Serves to delete class values.
        del self.__items[index]

    def __iter__(self):  # Serves to increment the interactor protocols.
        return self

    def __next__(self):  # # Serves to increment the interactor protocols.
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):  # Serves to print the class.
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):  # It serves as a representation for developers.
        return self.__str__()


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Adriano Santos')
    lista.add('Neide Ferreira')
    lista.add('Laura Beatriz')

    print(lista)

    lista[0] = 'João dos santos'
    lista[2] = 'Funciona?'

    print(lista)

    del lista[2]

    print(lista)

    for value in lista:
        print(value)

