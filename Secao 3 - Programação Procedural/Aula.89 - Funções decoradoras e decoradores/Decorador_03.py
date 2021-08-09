"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam.
ela retornando uma nova a ser usada no lugar.
"""

def decorar(funcao):
    print('\n1ª PASSO: Construindo def decorar(funcao)')
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('3ª PASSO: Executando def funcao_decorada()')
        print('------------------------------------------')
        print('4ª PASSO: Chamando funcao()')
        funcao()
        print('7ª PASSO: Executando def funcao_decorada()')
        print('------------------------------------------')

    return funcao_decorada


@decorar
def printar():
    print('5ª PASSO: Executando def printar()')
    for var in range(3):
        print('\t',var)
    print('6ª PASSO: Finalizado for var in range(3)')

print('2ª PASSO: Executando printar()')
printar()
print('8ª PASSO: Finalizado printar()')

# Saída:
# ############
# 0
# 1
# 2
# ############
#
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Curso-de-Python faz é X = decorador(X).
