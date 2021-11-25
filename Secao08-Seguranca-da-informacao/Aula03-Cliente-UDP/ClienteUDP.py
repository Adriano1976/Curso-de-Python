"""
- A Biblioteca Socket fornece acesso de baixo nível à interface de rede.
- O S.O. fornece a API socket que relaciona o programa com a rede.
- TCP (Transmission Control Protocol) ou Protocolo de Controle de Transmissão é um dos protocolos
de comunicação, que são suporte a rede global de internet, verificando se os dados são enviados na
seguência correta e sem erros.
- Nosso programa verificará se dados são enviados de maneira íntegra.
- O "PRINCÍPIO DA INTEGRIDADE" visa proteger a informação de alterações indevidas.
- UDP (User Datagram Protocol) ou Protocolo de Datagrama de Usuário é um protocolo simples da camada
de transporte que permite que a aplicação envie um datagrama dentro de um pacote IPv4 ou IPv6 a um
destino, porém sem qualquer tipo de grantia que o pacote chegue corretamente.
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket Criado com Sucesso!')

host = "localhost"
porta = 5433
mensagem = 'Oláaaaaa servidor!'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
