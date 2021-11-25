"""
- O ICMP (Internet Control Message Protocol), é um protocolo integrante do Protocolo IP utilizado
para fornecer relatórios de erros à fonte original.
- O ping é uma ferramenta que usa o protocolo ICMP para testar a conectividade entre nós.
É um comando disponível praticamente em todos os sistemas operacionais que consiste no envio de
pacotes para o equipamento de destino e na "escuta" das respostas.
- O "PRINCÍPIO DA DISPONIBILIDADE" visa garantir que um recurso e/ou informação esteja disponível.
- O módulo "os" fornece uma maneira simples de usar funcionalidades que são dependentes de
sistema operacional.
"""

import os

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: ', ip)
        print('-' * 60)
        os.system('ping ' + ip)
        print('-' * 60)
