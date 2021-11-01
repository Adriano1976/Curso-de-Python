"""
- JovaStript Object Notation - JSON.
- JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs.
"""
import json

print()
with open('Clientes.json', 'r') as arquivo:
    clients_data = json.load(arquivo)  # Abre e converte um arquivo de json para python.

with open('Produtos.json', 'r') as arquivo:
    product_data = json.load(arquivo)  # Abre e converte um arquivo de json para python.

print(clients_data)
print(product_data)
