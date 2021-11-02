"""
- Sempre que precisar executar várias tarefas simultâneas... Por tarefas, chamadas para funções
ou métodos... Isso pode acelerar o processo... Por tarefas simultâneas isso não que dizer que elas
serão executadas no mesmo momento, mas por diferentes threads do sistema.
- Uma outra aplicação também é com interfaces gráficas, geralmente quando você clica em um botão
que executa uma tarefa pesada, o próprio botão deve "travar" até a tarefa finalizar,
nesses casos usamos threads para garantir que a thread que manipula a 00-Interface vai ficar sempre
livre para que o usuário possa clicar em botões enquanto outras coisas acontecem ao mesmo tempo.
- O ideal é executar um thread até ele terminar, em seguida iniciar outro..
"""

from threading import Thread
from time import sleep


def funcao_do_t1(texto, tempo):
    sleep(tempo)
    print(texto)

    t = Thread(target=funcao_do_t2, args=('Eu sou o T2', 2))
    t.start()


def funcao_do_t2(texto, tempo):
    sleep(tempo)
    print(texto)

    t = Thread(target=funcao_do_t1, args=('Eu sou o T1', 2))
    t.start()


t1 = Thread(target=funcao_do_t1, args=('Eu sou o T1', 2))
t1.start()
