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

        dados = [
            ('Marcelo', 'Cardoso', 19, 55),
            ('Karla', 'Balbino', 45, 75.8),
            ('Augusto', 'Vasconcelos', 75, 65.5),
            ('Nádja', 'Ferreira', 55, 72),
            ('Cristiane', 'Brota', 45, 69)
        ]

        cursor.executemany(sql, dados)
        conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(f'{linha["id"]} | {linha["nome"]} {linha["sobrenome"]} - {linha["idade"]} - {linha["peso"]} ')
