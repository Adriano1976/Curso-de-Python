import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    database='clientes',
    user='root',
    password=''
)

# Buscando informações do banco de dados SE tiver conectado
if conexao.is_connected():
    db_info = conexao.get_server_info()
    print('Conectado ao servidor MySQL versão ', db_info)
    cursor = conexao.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)
    print()

# Executando os comando SQL
cursor.execute('SELECT * FROM clientes')
for linhas in cursor.fetchall():
    id, nome, sobrenome, idade, peso = linhas
    print(id, nome, sobrenome, idade, peso)

print()
# Encerrando a conexão com o banco de dados seguindo uma condição
if conexao.is_connected():
    cursor.close()
    conexao.close()
    print('Conexão ao MySQL foi encerrada')
