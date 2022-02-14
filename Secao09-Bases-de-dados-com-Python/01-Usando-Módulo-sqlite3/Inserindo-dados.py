import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Neide Ferreira", 60.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria Ester', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'João Carlos', 'peso': 25})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Joana Santos', 'peso': 25})

conexao.commit()

cursor.close()
conexao.close()
