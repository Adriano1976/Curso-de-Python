"""
- O que são dataclasses? O módulo Dataclasses fornece um decorador e funções para criar automaticamente
métodos, como __init__(), __repr__(), __eq__(etc) em classes definidas pelo usuário.
- Basicamente, dataclasses são syntax sugar para criar classes normais.
- Foi originalmente descrito na PEP 557.
- Adicionado na versão 3.7 do Curso-de-Python.
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
   p1 = Pessoa('Adriano', 'Cícero')
   p2 = Pessoa('Carlos', 'Tessio')
   p3 = Pessoa('Denilson', 'Quálity')
   p4 = Pessoa('Beatriz', 'Josebalde')

   pessoas = [p1, p2, p3, p4]

   print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
   print()

   print(p1)
   print(p2)
   print(p3)
   print(p4)
   print()

   print(asdict(p1))
   print(astuple(p1))
