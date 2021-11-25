"""
- A Biblioteca Socket fornece acesso de baixo n�vel � interface de rede.
- O S.O. fornece a API socket que relaciona o programa com a rede.
- TCP (Transmission Control Protocol) ou Protocolo de Controle de Transmiss�o � um dos protocolos
de comunica��o, que s�o suporte a rede global de internet, verificando se os dados s�o enviados na
segu�ncia correta e sem erros.
- Nosso programa verificar� se dados s�o enviados de maneira �ntegra.
- O "PRINC�PIO DA INTEGRIDADE" visa proteger a informa��o de altera��es indevidas.
- UDP (User Datagram Protocol) ou Protocolo de Datagrama de Usu�rio � um protocolo simples da camada
de transporte que permite que a aplica��o envie um datagrama dentro de um pacote IPv4 ou IPv6 a um
destino, por�m sem qualquer tipo de grantia que o pacote chegue corretamente.
"""
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
except socket.error as e:
    print('A conex�o falhou!')
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
    print(f'N�o foi poss�vel conectar no Host: "{HostAlvo}" - Porta: {PortaAlvo}')
    print(f'Erro: {e}')
    sys.exit()
