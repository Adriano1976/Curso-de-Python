from Classes import Escritor
from Classes import Caneta
from Classes import MaquinaDeEscrever

escritor = Escritor('Adriano Santos')
print(f'\nNome do Escritor: {escritor.nome}')

caneta = Caneta('Bic')
print(f'Marca da Caneta: {caneta.marca}')

maquina = MaquinaDeEscrever()
maquina.escrever()

print('\nASSOCIAÇÃO ENTRE AS CLASSES: Escritor - Caneta - MaquinaDeEscrever:\n')

escritor._ferramenta = caneta
escritor.ferramenta.escrever()
escritor._ferramenta = maquina
escritor.ferramenta.escrever()
