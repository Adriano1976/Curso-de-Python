""" Funções - def em Curso-de-Python (Parte 1) """
def funcao():
    print('Olá mundo!')

funcao()
funcao()

def saudacao (msg, nome):
    print(msg, nome)

saudacao('Olá', 'Adriano Santos')
saudacao('Hello', 'Neide Ferreira')


def saudacao1(msg='Olá', nome='Usuário'):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    return f'{msg} {nome}'

variavel = saudacao1()
print(variavel)

saudacao1('Olá', 'Adriano Santos')
saudacao1('Hello', 'Neide Ferreira')
saudacao1()