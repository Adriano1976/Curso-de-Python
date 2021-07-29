'''
Encapsulamento em outras linguagens: public, protected, private
Encapsulamento em Python: public ''
Encapsulamento em Python: protected '_' (public_)
Encapsulamento em Python: privado '__' (_NOMECLASSE__nometributo)

'''


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print([id], nome)

    def apagar_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

print('-=' * 30)
print('Antes da invasão e tentativa da mudança dos dados:'.upper())
bd.listar_clientes()
print(f'Dados: {bd.dados}\n')

print('-=' * 30)
print('Depois da invasão e com sucesso na mudança dos dados:'.upper())
bd.dados = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
print(f'Dados: {bd.dados}\n')
