"""
- Sempre que precisar executar várias tarefas simultâneas... Por tarefas, chamadas para funções
ou métodos... Isso pode acelerar o processo... Por tarefas simultâneas isso não que dizer que elas
serão executadas no mesmo momento, mas por diferentes threads do sistema.
- Uma outra aplicação também é com interfaces gráficas, geralmente quando você clica em um botão
que executa uma tarefa pesada, o próprio botão deve "travar" até a tarefa finalizar,
nesses casos usamos threads para garantir que a thread que manipula a 00-Interface vai ficar sempre
livre para que o usuário possa clicar em botões enquanto outras coisas acontecem ao mesmo tempo.
"""

from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olha eu passando 01!', 10))
t1.start()

while t1.is_alive():
    print('Estou esperando a thread.')
    sleep(2)

print('Thread acabou!')
