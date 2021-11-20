import tkinter as tk


class Tela:
    __slots__ = ['nossaTela', 'texto', 'entrada']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Tela Principal')

        self.texto = tk.Label(self.nossaTela, text='Insira seu nome: ', font='Verdana')
        self.texto.pack(side=tk.LEFT, pady=10)

        self.entrada = tk.Entry(self.nossaTela)
        self.entrada.pack(side=tk.LEFT, pady=10, padx=10)
        self.entrada.bind('<Return>', self.resposta)

    def resposta(self, event):
        print(f'Olá {self.entrada.get()}')


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
