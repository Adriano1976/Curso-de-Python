import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Joana Marquez', 'id': 2}
)

conexao.commit()

cursor.close()
conexao.close()
