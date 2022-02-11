from Controle_agenda import AgendaDB

#
# class AgendaDB:
#     # Abrindo a connecção do programa com a base de dados agenda
#     def __init__(self, arquivo):
#         self.conn = sqlite3.connect(arquivo)
#         self.cursor = self.conn.cursor()
#
#     # Inserindo registro na base de dados agenda
#     def inserir(self, nome, telefone):
#         consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
#         self.cursor.execute(consulta, (nome, telefone))
#         self.conn.commit()
#
#     # Listando todos registros da base de dados agenda
#     def listar(self):
#         self.cursor.execute('SELECT * FROM agenda')
#         for linha in self.cursor.fetchall():
#             id, nome, telefone = linha
#             print(f'{id} | {nome} | {telefone}')
#
#     # Buscando registros da base de dados agenda por meio de buscas
#     def buscar(self, valor):
#         consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
#         self.cursor.execute(consulta, (f'%{valor}%',))
#         for linha in self.cursor.fetchall():
#             id, nome, telefone = linha
#             print(f'{id} | {nome} | {telefone}')
#
#     # Alterando registro na base de dados agenda
#     def editar(self, nome, telefone, id):
#         consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
#         self.cursor.execute(consulta, (nome, telefone, id))
#         self.conn.commit()
#
#     # Excluindo registro na base de dados agenda
#     def excluir(self, id):
#         consulta = 'DELEFONE FROM agenda WHERE id=?'
#         self.cursor.execute(consulta, (id,))
#         self.conn.commit()
#
#     # Encerrando a connecção do programa com a base de dados agenda
#     def fechar(self):
#         self.cursor.close()
#         self.conn.close()


if __name__ == '__main__':

    controle = True
    while controle:
        print('----------------------------------------------------------------------------')
        print('------------------------------ AGENDA PESSOAL ------------------------------')
        print('----------------------------------------------------------------------------')
        print('1 - Inserir | 2 - Listar | 3 - Buscar | 4 - Alterar | 5 - Excluir | 6 - Sair')

        option = int(input('\nDigite a opção desejada: '))

        # Inserindo registro na base de dados agenda.db -------------------------------------
        if option == 1:
            print('-------------------------------------------------------')
            print('----------- INSERINDO INFORMAÇÕES NA AGENDA -----------')
            print('-------------------------------------------------------')
            print()
            agenda = AgendaDB('agenda.db')
            nome = input('Digite o nome completo: ')
            telefone = input('Digite o telefone: ')
            agenda.inserir(nome, telefone)
            opcao = int(input('\nDeseja continuar?\n Sim - 1 | Não - 0:  '))
            print()
            if opcao != 1:
                break
            else:
                continue

        # Listando registro da base de dados agenda.db --------------------------------------
        if option == 2:
            print('-------------------------------------------------------')
            print('---------- LISTANDO AS INFORMAÇÕES DA AGENDA ----------')
            print('-------------------------------------------------------')
            print()
            agenda = AgendaDB('agenda.db')
            agenda.listar()
            opcao = int(input('\nDeseja continuar?\n Sim - 1 | Não - 0:  '))
            print()
            if opcao != 1:
                print('Encerrando o programa ...')
                break
            else:
                continue

        # Buscando registro na base de dados agenda.db --------------------------------------
        if option == 3:
            print('-------------------------------------------------------')
            print('------------ BUSCANDO INFORMAÇÕES NA AGENDA -----------')
            print('-------------------------------------------------------')
            print()
            agenda = AgendaDB('agenda.db')
            nome = input('Digite o nome completo: ')
            print()
            agenda.buscar(nome,)
            opcao = int(input('\nDeseja continuar?\n Sim - 1 | Não - 0:  '))
            print()
            if opcao != 1:
                print('Encerrando o programa ...')
                break
            else:
                continue

        # Editando registro na base de dados agenda.db --------------------------------------
        if option == 4:
            print('-------------------------------------------------------')
            print('------------ EDITANDO INFORMAÇÕES NA AGENDA -----------')
            print('-------------------------------------------------------')
            print()
            agenda = AgendaDB('agenda.db')
            nome = input('Digite o nome completo: ')
            telefone = input('Digite o telefone: ')
            id = int(input('Digite o código: '))
            agenda.editar(nome, telefone, id)
            opcao = int(input('\nDeseja continuar?\n Sim - 1 | Não - 0:  '))
            print()
            if opcao != 1:
                print('Encerrando o programa ...')
                break
            else:
                continue

        # Excluindo registro na base de dados agenda.db -------------------------------------
        if option == 5:
            print('-------------------------------------------------------')
            print('----------- EXCLUINDO INFORMAÇÕES DA AGENDA -----------')
            print('-------------------------------------------------------')
            print()
            agenda = AgendaDB('agenda.db')
            id = int(input('Digite o código'))
            agenda.excluir(id,)
            opcao = int(input('\nDeseja continuar?\n Sim - 1 | Não - 0:  '))
            print()
            if opcao != 1:
                print('Encerrando o programa ...')
                break
            else:
                continue

        # Fechando o programa e saindo da base de dados agenda.db ---------------------------
        if option == 6:
            print()
            print('Encerrando o programa ...')
            agenda = AgendaDB('agenda.db')
            agenda.fechar()
            break
