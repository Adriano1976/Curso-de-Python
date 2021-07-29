def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi():
    print('OI Adriano.')

@master
def outra_funcao(msg):
    print(msg)


fala_oi()

