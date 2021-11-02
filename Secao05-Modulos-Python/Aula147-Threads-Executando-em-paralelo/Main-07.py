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

# Uma variável global para obter os resultados
resultados = []


def vou_ser_um_thread(lista):
    # Uma função resolveria seu problema

    # Não entendi o motivo do for no seu código
    # ou faltou algum detalhe
    # então eu removi
    resultados.append(''.join(lista))


# As listas
lista_1 = ['1', '2', '3', '4', '5', '6']
lista_2 = ['6', '5', '4', '3', '2', '1']

# Os Threads
t1 = Thread(target=vou_ser_um_thread, args=(lista_1,))
t2 = Thread(target=vou_ser_um_thread, args=(lista_2,))
t1.start()
t2.start()
t1.join()
t1.join()

print(f'\nResultados: {resultados}')
