'''
Encapsulamento em outras linguagens: public, protected, private
Encapsulamento em Python: public ''
Encapsulamento em Python: protected '_' (privado mais fraco)
Encapsulamento em Python: privado '__' (_NOMECLASSE__nometributo)
'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, '-', nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

print('-=' * 30)
print('Antes da invasão e tentativa da mudança dos dados:'.upper())
bd.listar_clientes()
print(f'Dados: {bd._BaseDeDados__dados}')
print(f'Dados: {bd.dados}\n')

print('-=' * 30, '')
print('Durante da invasão e tentativa da mudança dos dados:'.upper())
bd.__dados = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print(f'Dados: {bd.__dados}')
bd.__dados = 'Outro valor qualquer'  # Mudando os dados.
print(f'Dados: {bd.__dados}\n')  # Depois da invasão e sucesso na mudança dos dados.

print('-=' * 30)
print('Depois da invasão, porém sem sucesso na mudança dos dados:'.upper())
bd.listar_clientes()
print(f'Dados: {bd._BaseDeDados__dados}')
print(f'Dados: {bd.dados}\n')

