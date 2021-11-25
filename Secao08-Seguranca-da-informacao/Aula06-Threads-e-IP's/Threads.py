"""
- Thread é o processo e no ambiente "multithread", cada processo pode responder a vários solicitações
concorrentemente ou mesmo simultaneamente.
- A biblioteca "Multithreading" constrói interfaces de alto nível para processamento usando o módulo Thread,
de mais baixo nível, ou seja, relação direta com o processador.
"""

import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} - Km: {trajeto} ')


t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[2, 'Python'])

t_carro1.start()
t_carro2.start()
