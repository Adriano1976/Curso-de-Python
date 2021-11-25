"""
- A Biblioteca "json" serve para fornece operação de codificação e decodificação JSON.
- A funções e classes "urllib.request import urlopen" serve para ajudar a abrir as URLs.
"""


import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
host = dados['hostname']
org = dados['org']
cid = dados['city']
pais = dados['country']
reg = dados['region']
local = dados['loc']
cod_postal = dados['postal']
font = dados['readme']

print('DETALHES DO IP EXTERNO:\n')
print(f'IP: {ip}\n'
      f'Host: {host}\n'
      f'Cidade: {cid}\n'
      f'Região: {reg}\n'
      f'País: {pais}\n'
      f'Localização: {local}\n'
      f'CEP: {cod_postal}\n'
      f'Org.: {org}')
