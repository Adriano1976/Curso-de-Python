"""
- O ICMP (Internet Control Message Protocol), ? um protocolo integrante do Protocolo IP utilizado
para fornecer relat?rios de erros ? fonte original.
- O ping ? uma ferramenta que usa o protocolo ICMP para testar a conectividade entre n?s.
? um comando dispon?vel praticamente em todos os sistemas operacionais que consiste no envio de
pacotes para o equipamento de destino e na "escuta" das respostas.
- O "PRINC?PIO DA DISPONIBILIDADE" visa garantir que um recurso e/ou informa??o esteja dispon?vel.
- O m?dulo "os" fornece uma maneira simples de usar funcionalidades que s?o dependentes de
sistema operacional.
"""

import os

# Ao informar o ip ou host, fazer dessa forma: "ip" ou "host" em aspas.
ip_ou_host = input('\nDigite o ip ou host a ser verificado: ')

print()
print(f'Verificando o IP: {ip_ou_host}')

print('-' * 60)
os.system(f'ping -n 6 "{ip_ou_host}"')
print('-' * 60)
