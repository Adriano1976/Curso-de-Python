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

from Carro import Car

if __name__ == '__main__':
  # Código cliente
  carro = Car()

  carro.acelerar()  # 1
  carro.acelerar()  # 2
  carro.acelerar()  # 3
  carro.frear()  # 2
  carro.frear()  # 1
  carro.frear()  # 0
  carro.frear()  # 0

  print(carro.aceleracao)  # 0