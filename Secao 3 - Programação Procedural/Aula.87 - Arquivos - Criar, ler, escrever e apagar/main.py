import json

d1 = {
    'Pessoa 1': {
        'nome:': 'Luiz Augusto',
        'idade:': 25,
    },
    'Pessoa 2': {
        'nome:': 'Adriano Santos',
        'idade:': 30,
    },
}

print()
print(d1,'\n')

d1_json = json.dumps(d1, indent=True)

with open('arquivo.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
