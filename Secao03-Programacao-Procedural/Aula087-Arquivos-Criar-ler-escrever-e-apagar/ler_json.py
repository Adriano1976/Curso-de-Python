import json
from time import sleep

with open('arquivo.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

print()
for chave, var in d1_json.items():
    print(chave)
    sleep(1.3)
    for chave1, var1 in var.items():
        print(chave1, var1)
        sleep(1.3)
    print()


