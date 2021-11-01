"""
- JovaStript Object Notation - JSON.
- JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs.
"""
from Dados import *
import json

print()
print(lista)
print(type(lista))
lista_json = json.dumps(lista)  # Convertendo um string python para string json.
print(lista_json)
print(type(lista_json))
print()

print(clientes_dict)
print(type(clientes_dict))
clientes_json = json.dumps(clientes_dict, indent=4)  # Convertendo um string python para string json.
print(clientes_json)
print(type(clientes_json))
print()
