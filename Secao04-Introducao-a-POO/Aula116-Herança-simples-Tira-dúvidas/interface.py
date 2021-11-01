from biblioteca import Biblioteca


class Interface(Biblioteca):
    def metodo_da_interface(self):
        print('Sou o método da Interface.')

    def outro_metodo_da_interface(self):
        print(f'Eu ou outro método da Interface.')
