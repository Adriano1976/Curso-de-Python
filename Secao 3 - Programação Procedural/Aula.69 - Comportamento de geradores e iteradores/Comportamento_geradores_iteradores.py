print('\n------------------ iterador --------------------------------')

nome = 'Adriano Santos'
iterador = iter(nome) # Converte uma string em iterador

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print('\nOlhar o for')

for var in iterador:
    print(var)

print('\n------------------ gerador --------------------------------')

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('\nOlhar o for')

for var in gerador:
    print(var)

