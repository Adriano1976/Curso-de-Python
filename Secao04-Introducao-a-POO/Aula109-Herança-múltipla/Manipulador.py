"""
- O método que é usado para obter um valor (o getter) é decorado com @property.
- O método que é usado para retornar uma cópia (o setter) é decorado com @xxxx.setter.
- Embora __slots__ seja muito utilizado para não permitir que usuários de nossas classes criem outros atributos,
ele avisa o Curso-de-Python para não usar um dicionário e apenas alocar espaço para um conjunto fixo de atributos.
- Um mix-in	é uma classe que não se destina a ser independente - existe	para adicionar funcionalidade
extra a	outra classe através de	herança	múltipla.
- Os programadores,	por	convenção e	para deixar	explícito a	classe como	um mix-in, colocam o termo
'MixIn' no nome	da classe.
- Cada mix-in é responsável	por	fornecer uma peça específica de	funcionalidade opcional.
- Repare que nossos	mix-ins não	têm um método __init__(), pois fornecem métodos adicionais.
- Cada mix-in é responsável por fornecer uma peça específica de funcionalidade opcional.
"""


class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()

        return total
