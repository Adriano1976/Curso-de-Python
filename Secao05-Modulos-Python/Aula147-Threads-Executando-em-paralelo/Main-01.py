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


class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(10):
    print(i)
    sleep(1)
