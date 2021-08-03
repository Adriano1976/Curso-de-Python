"""
- JovaStript Object Notation - JSON.
- JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs.
"""
from Dados import *
import json

print()
print(clientes_dict)
print(type(clientes_dict))

clientes_json = json.dumps(clientes_dict, indent=4)

print(clientes_json)
print(type(clientes_json))
print()

clientes_dict = json.loads(clientes_json)  # Convertendo uma string json para string python.

print(clientes_dict)
print(type(clientes_dict))
print()
