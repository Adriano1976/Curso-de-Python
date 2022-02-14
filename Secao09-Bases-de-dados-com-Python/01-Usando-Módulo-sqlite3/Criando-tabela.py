import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS clientes('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)

conexao.commit()

cursor.close()
conexao.close()
