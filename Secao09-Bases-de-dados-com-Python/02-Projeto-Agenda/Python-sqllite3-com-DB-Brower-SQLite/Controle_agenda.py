import sqlite3


class AgendaDB:
    # Abrindo a connecção do programa com a base de dados agenda
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    # Inserindo registro na base de dados agenda
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    # Listando todos registros da base de dados agenda
    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(f'{id} | {nome} | {telefone}')

    # Buscando registros da base de dados agenda por meio de buscas
    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(f'{id} | {nome} | {telefone}')

    # Alterando registro na base de dados agenda
    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    # Excluindo registro na base de dados agenda
    def excluir(self, id):
        consulta = 'DELEFONE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    # Encerrando a connecção do programa com a base de dados agenda
    def fechar(self):
        self.cursor.close()
        self.conn.close()
