import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS clientes('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'nome TEXT,'
#     'peso REAL'
#     ')'
# )

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Adriano Santos", 80.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria Ester', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'João Carlos', 'peso': 25})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Joana Santos', 'peso': 25})

conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
