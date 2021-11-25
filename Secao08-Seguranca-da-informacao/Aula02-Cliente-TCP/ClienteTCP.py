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
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
except socket.error as e:
    print('A conexão falhou!')
    print(f'Erro: {e}')
    sys.exit()

print("Socket criado com sucesso")

HostAlvo = input('Digite o Host ou Ip a ser conectado: ')
PortaAlvo = input('Digite a porta a ser conectada: ')

try:
    s.connect((HostAlvo, int(PortaAlvo)))
    print(f'Cliente TCP conectado com Sucesso no Host: "{HostAlvo}" e na Porta: "{PortaAlvo}"')
    s.shutdown(2)
except socket.error as e:
    print(f'Não foi possível conectar no Host: "{HostAlvo}" - Porta: {PortaAlvo}')
    print(f'Erro: {e}')
    sys.exit()
