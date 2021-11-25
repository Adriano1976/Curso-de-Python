"""
LISTA DAS PRINCIPAIS PORTAS:

FTP - 21    	        HTTP - 80	            DNS - 53
SSH - 22    	        HTTPS - 443	            SMTP - 25
TELNET - 23 	        POP3 - 110	            SQUID - 3128
SFTP - 115  	        IMAP - 143	            SMTP - 587
TÚNEL PPTP - 1723   	RDP - 3389	            BGP - 179
SNMP - 161  	        IMAP4 - 143	            DHCP - 67
DHCP - 68   	        MYSQL - 3306	        Microsoft SQL - 1443

AS TOP PORTAS MAIS VULNERÁVEIS
TCP - 22 *          TCP - 443 *             TCP - 80 *              TCP - 3389
TCP - 3301          TCP - 3306              TCP - 8080              TCP - 53
TCP - 9002          TCP - 5986              TCP - 8443              FTP - 20
FTP - 21
"""

import socket
from Cores import Cor

ip = input(f'{Cor.AZUL}Digite o host para consulta: ')

ports = []
contador = 0

while contador < 10:
    ports.append(int(input(f'{Cor.NEGRITO}Informe o nº da porta para verificação: ')))
    contador += 1

print()
for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print(f'{Cor.VERDE}No momento a porta {port} do IP {ip} está Aberta/Acessível. ')
    else:
        print(f'{Cor.VERMELHO}No momento a porta {port} do IP {ip} está Fechada/Inacessível.')

print(f'\nO Scanner foi finalizado com sucesso!')
