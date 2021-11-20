import tkinter as tk
from tkinter import messagebox


class Tela:
    __slots__ = ['nossaTela', 'lbl']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela Principal')

        # self.coisa = tk.NomeDoWidget(WidgetPai, opcaoDeConfiguração)
        self.lbl = tk.Label(
            self.nossaTela,
            text='Abrir Caixa de Mensagem',
            font=('Verdana', '20'),
            pady='20',
            background='orange',
            relief='raised')
        self.lbl.pack(ipadx=20, pady=30)
        self.lbl.bind('<Button>', self.resposta)

    def resposta(self, event):
        messagebox.showinfo('Caixa de Mensagem', 'Isso é uma mensagem')


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
