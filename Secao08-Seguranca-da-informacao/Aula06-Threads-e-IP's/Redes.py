"""
- A Biblioteca "ipaddress" tem a capacidade de criar, manipular endereços IP do tipo IPv4, IPv6 e até redes inteiras.
"""

import ipaddress

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)

print(f'Endereço da rede: {rede}')
for ip in rede:
    print(f'Endereço de ip: {ip}')
