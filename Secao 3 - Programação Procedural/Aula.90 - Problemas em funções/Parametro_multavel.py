def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício Gomes', 'Fernando Souza']
clientes1 = lista_de_clientes(['José Carlos', 'Maria José', 'Eduardo Pazuello', 'Neide Ferreira'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos Aurélio', 'Jonas Souza', 'Zico Gomes', 'Roberto de Souza', 'Roberto Carlos'])
clientes3 = lista_de_clientes(['José de Paula', 'Carlos Alberto', 'Eridivan Nascimento', 'José Edjânio'])

print('\n-----------------------------------')
print('  Lista de Clientes - Prospéctos')
print('-----------------------------------')
for var in clientes1:
    print('\tNome:', var)

print('\n-----------------------------------')
print('  Lista de Clientes - Devedores')
print('-----------------------------------')
for var in clientes2:
    print('\tNome:', var)

print('\n-----------------------------------')
print('  Lista de Clientes - Bom Pagador')
print('-----------------------------------')
for var in clientes3:
    print('\tNome:', var)
