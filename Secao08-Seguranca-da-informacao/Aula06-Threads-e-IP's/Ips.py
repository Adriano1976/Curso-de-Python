"""
- A Biblioteca "ipaddress" tem a capacidade de criar, manipular endereços IP do tipo IPv4, IPv6 e até redes inteiras.
"""

import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(f'1 - Endereço do ip: {endereco}')
print(f'2 - Endereço do ip: {endereco + 100}')
print(f'3 - Endereço do ip: {endereco + 257}')
print(f'4 - Endereço do ip: {endereco + 256}')
print(f'5 - Endereço do ip: {endereco + 2000}')
