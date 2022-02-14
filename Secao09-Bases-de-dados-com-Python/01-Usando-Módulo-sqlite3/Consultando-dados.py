import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    id, nome, peso = linha

    print(id, nome, peso)

cursor.close()
conexao.close()
