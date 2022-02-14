import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()
