import tkinter as tk


class Tela:
    __slots__ = ['nossaTela', 'fr1', 'fr2', 'lbl1', 'lbl2', 'lbl3', 'lbl4', 'lbl5']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela Principal')

        # self.coisa = tk.nomeDoWidget(widgetPai, opcoesDeConfiguracao)
        self.fr1 = tk.Frame(self.nossaTela)
        self.fr2 = tk.Frame(self.nossaTela)

        self.fr1.pack()
        self.fr2.pack(side=tk.BOTTOM)

        self.lbl1 = tk.Label(self.fr1, text='Estou no Frame 1', font=('Arial', '16'), pady=5, padx=10)
        self.lbl1.pack(side=tk.LEFT)

        self.lbl2 = tk.Label(self.fr1, text='Estou no Frame 1', font=('Arial', '16'), pady=5, padx=10)
        self.lbl2.pack(side=tk.LEFT)

        self.lbl3 = tk.Label(self.fr1, text='Estou no Frame 1', font=('Arial', '16'), pady=5, padx=10)
        self.lbl3.pack(side=tk.LEFT)

        self.lbl4 = tk.Label(self.fr2, text='Estou no Frame 2', font=('Arial', '16'), pady=5, padx=10)
        self.lbl4.pack(side=tk.LEFT)

        self.lbl5 = tk.Label(self.fr2, text='Estou no Frame 2', font=('Arial', '16'), pady=5, padx=10)
        self.lbl5.pack(side=tk.LEFT)


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
