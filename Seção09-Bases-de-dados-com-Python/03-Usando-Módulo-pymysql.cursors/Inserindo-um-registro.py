from contextlib import contextmanager

import pymysql.cursors


@contextmanager
def conecta():
    conexao = pymysql.connect(
        # host='127.0.0.1',
        host='localhost',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 110, 220))
        conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(f'{linha["id"]} | {linha["nome"]} {linha["sobrenome"]} - {linha["idade"]} - {linha["peso"]} ')
