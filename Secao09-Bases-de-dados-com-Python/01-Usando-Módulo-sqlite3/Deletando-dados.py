import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute(
    'DELETE FROM clientes WHERE id=:id', {'id': 2}
)

conexao.commit()

cursor.close()
conexao.close()
