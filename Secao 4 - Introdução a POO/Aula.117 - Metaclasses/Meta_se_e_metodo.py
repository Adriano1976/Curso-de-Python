"""
- Quer saber se é um Método:
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'B':
            if "b_fala" not in namespace or not callable(namespace['b_fala']):
                print("\nFalta MÉTODO 'b_fala' na classe B!")
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    # b_fala = "Aqui vai dar erro."

    def b_fala():
        print("Aqui vai passar normal")
