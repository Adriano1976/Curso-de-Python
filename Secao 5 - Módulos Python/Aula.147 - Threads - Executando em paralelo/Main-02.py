"""
- Sempre que precisar executar várias tarefas simultâneas... Por tarefas, chamadas para funções
ou métodos... Isso pode acelerar o processo... Por tarefas simultâneas isso não que dizer que elas
serão executadas no mesmo momento, mas por diferentes threads do sistema.
- Uma outra aplicação também é com interfaces gráficas, geralmente quando você clica em um botão
que executa uma tarefa pesada, o próprio botão deve "travar" até a tarefa finalizar,
nesses casos usamos threads para garantir que a thread que manipula a interface vai ficar sempre
livre para que o usuário possa clicar em botões enquanto outras coisas acontecem ao mesmo tempo.
"""

from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olha eu passando 01!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olha eu passando 02!', 3))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olha eu passando 03!', 1))
t3.start()

for i in range(15):
    print(i)
    sleep(.5)
