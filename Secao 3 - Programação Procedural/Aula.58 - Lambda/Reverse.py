'''
- O parâmetro reverse, inverte a ordem da ordenação (de crescente para decrescente).
- É igual para .sort ou sorted.
'''

letras = ['b', 'c', 'e', 'd', 'a']

# com reverse=True, ao invés de ordem crescente, teremos ordem decrescente
novas_letras = sorted(letras, reverse=True)
print(novas_letras)  # ['e', 'd', 'c', 'b', 'a']
