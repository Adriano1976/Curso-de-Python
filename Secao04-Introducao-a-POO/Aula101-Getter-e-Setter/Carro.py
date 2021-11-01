"""
- Getters e Setters geralmente são usados para modificar o código sem ter que mudar onde você já escreveu
e testou código antigo... Ex.: imagine que eu tenho uma classe carro...
- Ele é bem simples e eu tenho acesso à aceleração. Só que eu tenho um código cliente que usa essa classe
e esse código está escrito em mais de mil arquivos.
- Até ontem, a aceleração podia passar para negativo, porém hoje nosso gerente resolveu que a aceleração
nunca pode passar para negativo.
- Qual você escolhe, editar a classe ou editar os mil arquivos que usam o código cliente? Usando getters
e setters é super simples fazer a alteração, nenhum código cliente vai nem notar a diferença.
"""


class Car:
    def __init__(self):
        self._aceleracao = 0

    def acelerar(self):
        self.aceleracao += 1
        print(f'Acelerando para {self.aceleracao}ª macha.')

    def frear(self):
        self.aceleracao -= 1
        print(f'freando para {self.aceleracao}ª macha.')

    @property
    def aceleracao(self):
        return self._aceleracao

    @aceleracao.setter
    def aceleracao(self, valor):
        if valor <= 0:
            self._aceleracao = 0
        else:
            self._aceleracao = valor
