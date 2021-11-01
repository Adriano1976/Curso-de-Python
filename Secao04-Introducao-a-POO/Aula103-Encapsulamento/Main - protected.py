'''
Encapsulamento em outras linguagens: public, protected, private
Encapsulamento em Curso-de-Python: public ''
Encapsulamento em Curso-de-Python: protected '_' (privado mais fraco)
Encapsulamento em Curso-de-Python: privado '__' (_NOMECLASSE__nometributo)

'''


class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, '-', nome)

    def apagar_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

print('-=' * 30)
print('Antes da invasão e tentativa da mudança dos dados:'.upper())
bd.listar_clientes()
print(f'Dados: {bd._dados}\n')

print('-=' * 30)
print('Depois da invasão e com sucesso na mudança dos dados:'.upper())
bd._dados = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print(f'Dados: {bd._dados}\n')
