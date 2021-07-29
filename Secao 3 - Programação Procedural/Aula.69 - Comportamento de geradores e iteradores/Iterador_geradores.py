from time import sleep


def demora(msg):
    """Função que demora 1 segundo pra me responder"""
    sleep(1)
    return msg


def gerador(o_que_fazer):
    """ Gerador """
    yield o_que_fazer('Oi')
    yield o_que_fazer('Eu')
    yield o_que_fazer('vou')
    yield o_que_fazer('demorar.')


g = gerador(demora)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
