from time import sleep

exemplo = {
    '1ª Pessoa -->': {'Nome': 'João', 'Sobrenome': 'Cardoso', 'Idade': 28},
    '2ª Pessoa -->': {'Nome': 'Carla', 'Sobrenome': 'Vieira', 'Idade': 53},
    '3ª Pessoa -->': {'Nome': 'Santoro', 'Sobrenome': 'Conrado', 'Idade': 49},
    '4ª Pessoa -->': {'Nome': 'Jivago', 'Sobrenome': 'Sendas', 'Idade': 89},
    '5ª Pessoa -->': {'Nome': 'Margareth', 'Sobrenome': 'Taylor', 'Idade': 64},
    '6ª Pessoa -->': {'Nome': 'Luiz', 'Sobrenome': 'Miranda', 'Idade': 35}
}

print()
for var in exemplo.items():
    print(var)
    sleep(1.3)


