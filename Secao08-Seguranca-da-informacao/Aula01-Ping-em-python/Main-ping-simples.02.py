"""
- O ICMP (Internet Control Message Protocol), é um protocolo integrante do Protocolo IP utilizado
para fornecer relatórios de erros à fonte original.
- O ping é uma ferramenta que usa o protocolo ICMP para testar a conectividade entre nós.
É um comando disponível praticamente em todos os sistemas operacionais que consiste no envio de
pacotes para o equipamento de destino e na "escuta" das respostas.
- O "PRINCÍPIO DA DISPONIBILIDADE" visa garantir que um recurso e/ou informação esteja disponível.
- O módulo "os" fornece uma maneira simples de usar funcionalidades que são dependentes de
sistema operacional.
"""

import tkinter as tk
import os


class Tela:
    __slots__ = ['nossaTela', 'texto', 'btn', 'entrada', 'ping']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Tela Principal do Verificador do Sistema via PING')

        self.texto = tk.Label(self.nossaTela, text='Digite o ip ou host a ser verificado: ', font='Verdana')
        self.texto.pack(side=tk.LEFT, pady=30, padx=10)

        self.entrada = tk.Entry(self.nossaTela, font='Verdana')
        self.entrada.pack(side=tk.LEFT, pady=30, padx=10)

        self.btn = tk.Button(self.nossaTela, text='Verificar Ping', font='Verdana', bg='FireBrick',
                             fg='white', width=15, height=3, command=self.resposta)
        self.btn.pack(side=tk.LEFT, pady=30, padx=30)

    def resposta(self):
        print()
        print(f'Verificando o IP: {self.entrada.get()}')
        print('-' * 60)

        os.system(f'ping -n 6 "{self.entrada.get()}"')

        with open('log.txt', 'a+') as file:
            file.write(f'- {self.entrada.get()}\n')
            print('-' * 60)


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
