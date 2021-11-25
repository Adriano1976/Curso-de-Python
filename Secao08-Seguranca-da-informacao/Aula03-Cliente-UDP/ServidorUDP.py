import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket Criado com Sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nServidor: Oláaa Cliente e ai, Beleza?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviaando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)
