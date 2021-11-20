import tkinter


class Tela:
    __slots__ = ['nossaTela', 'lb1', 'lb2']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Progrmação em Python')

        self.lb1 = tkinter.Label(self.nossaTela, text='Estou estudando Python', background='red')
        self.lb1['font'] = ('Verdana', '18')
        self.lb1.pack(pady=20)

        self.lb2 = tkinter.Label(self.nossaTela, text='Agora vou estudar GBDs', background='blue')
        self.lb2['font'] = ('Verdana', '18')
        self.lb2.pack(ipadx=25, ipady=10)


if __name__ == '__main__':
    janelaRaiz = tkinter.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
