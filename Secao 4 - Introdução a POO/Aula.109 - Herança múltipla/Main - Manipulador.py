"""
- O método que é usado para obter um valor (o getter) é decorado com @property.
- O método que é usado para retornar uma cópia (o setter) é decorado com @xxxx.setter.
- Embora __slots__ seja muito utilizado para não permitir que usuários de nossas classes criem outros atributos,
ele avisa o Python para não usar um dicionário e apenas alocar espaço para um conjunto fixo de atributos.
- Um mix-in	é uma classe que não se destina a ser independente - existe	para adicionar funcionalidade
extra a	outra classe através de	herança	múltipla.
- Os programadores,	por	convenção e	para deixar	explícito a	classe como	um mix-in, colocam o termo
'MixIn' no nome	da classe.
- Cada mix-in é responsável	por	fornecer uma peça específica de	funcionalidade opcional.
- Repare que nossos	mix-ins não	têm um método __init__(), pois fornecem métodos adicionais.
- Cada mix-in é responsável por fornecer uma peça específica de funcionalidade opcional.
"""

if __name__ == '__main__':
    from Conta import ContaCorrente, SeguroDeVida
    from Manipulador import ManipuladorDeTributaveis

    cc1 = ContaCorrente('0002145-8', 'José Carlos', 1000.0)
    cc2 = ContaCorrente('2514005-5', 'João Batista', 1000.0)
    seguro1 = SeguroDeVida(100.0, 'José Carlos', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria José', '237-98')

    lista_tributaveis = [cc1, cc2, seguro1, seguro2]

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(f'Total de Tributos: {total}')
