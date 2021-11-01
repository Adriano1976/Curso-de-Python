"""
- JovaStript Object Notation - JSON.
- JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs.
"""
from Dados import *
import json

print()
with open('Clientes.json', 'w') as arquivo:
    json.dump(clientes_dict, arquivo, indent=4)  # Converte um arquivo python para json e cria 1 arquivo.

with open('Produtos.json', 'w') as arquivo:
    json.dump(produtos_dict, arquivo, indent=4)  # Converte um arquivo python para json e cria 1 arquivo.
