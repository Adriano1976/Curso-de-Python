"""
- Não use argumentos padrão mutáveis, a menos que você tenha um motivo REALMENTE bom para fazer isso.
- Uma lista vazia foi usada como um argumento padrão para uma função.
- Ao passar um valor mutável como um argumento padrão em uma função, o argumento padrão é alterado sempre
que esse valor é alterado.
- Aqui, "valor mutável" se refere a qualquer coisa como uma lista, um dicionário ou até mesmo uma
instância de classe.
- Como você pode ver, o Python "retém" o valor padrão e o vincula à função de alguma forma. No
final, usamos um padrão diferente cada vez que a função é chamada
"""


def append_01(element, seq=[]):  # Uma lista vazia foi usada como um argumento padrão para uma função.
    seq.append(element)
    return seq


def append_02(element, seq=None):  # Use None como padrão e atribua o valor mutável dentro da função.
    if seq is None:
        seq = [element]
    return seq


def compute_patterns_01(inputs=[]):  # Uma lista vazia foi usada como um argumento padrão para uma função.
    inputs.append('some stuff')
    patterns = ['a list based on'] + inputs
    return patterns


def compute_patterns_02(inputs=None):  # Use None como padrão e atribua o valor mutável dentro da função.
    if inputs is None:
        inputs = []
    inputs.append('some stuff')
    patterns = ['a list based on'] + inputs
    return patterns


if __name__ == '__main__':
    print()
    print(compute_patterns_01())
    print(compute_patterns_01())
    print(compute_patterns_01())
    print(compute_patterns_01())
    print(compute_patterns_01())
    print(compute_patterns_01())

    print()
    print(compute_patterns_02())
    print(compute_patterns_02())
    print(compute_patterns_02())
    print(compute_patterns_02())
    print(compute_patterns_02())
    print(compute_patterns_02())
