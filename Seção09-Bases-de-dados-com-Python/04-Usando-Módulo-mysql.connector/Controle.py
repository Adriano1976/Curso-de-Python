from Conexao import criar_conexao, fechar_conexao


def insere_usuario(iu_conection, nome, sobrenome, idade, peso):
    cursor = iu_conection.cursor()
    sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
    valores = (nome, sobrenome, idade, peso)
    cursor.execute(sql, valores)
    cursor.close()
    iu_conection.commit()
    print('Registro inserido e salvo com sucesso!\n')


def consulta_registro(cr_conection):
    cursor = cr_conection.cursor()
    sql = 'SELECT id, nome, sobrenome, idade, peso FROM clientes.clientes'
    cursor.execute(sql)

    for (id, nome, sobrenome, idade, peso) in cursor:
        print(id, nome, sobrenome, idade, peso)


def main():
    m_conection = criar_conexao('localhost', 'root', '251097anl', 'clientes')
    insere_usuario(m_conection, 'Antony', 'Cesar', 88, 28)
    consulta_registro(m_conection)
    fechar_conexao(m_conection)
    print('\nConexão ao MySQL foi encerrada ...')
