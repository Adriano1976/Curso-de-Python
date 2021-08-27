"""
- Sempre que precisar executar várias tarefas simultâneas... Por tarefas, chamadas para funções
ou métodos... Isso pode acelerar o processo... Por tarefas simultâneas isso não que dizer que elas
serão executadas no mesmo momento, mas por diferentes threads do sistema.
- Uma outra aplicação também é com interfaces gráficas, geralmente quando você clica em um botão
que executa uma tarefa pesada, o próprio botão deve "travar" até a tarefa finalizar,
nesses casos usamos threads para garantir que a thread que manipula a interface vai ficar sempre
livre para que o usuário possa clicar em botões enquanto outras coisas acontecem ao mesmo tempo.
"""

from threading import Thread, Lock
from time import sleep


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque(s).')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(15)
    threads = []

    print(f'\nIngressos em estoque: {ingressos.estoque}\n')
    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(f'\nIngressos em estoque: {ingressos.estoque}')
