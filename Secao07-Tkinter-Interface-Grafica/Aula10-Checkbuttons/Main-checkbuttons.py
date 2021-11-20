import tkinter as tk


class Tela:
    __slots__ = ['nossaTela', 'cb1', 'cb2', 'cb3', 'cb4', 'var1', 'var2', 'var3','var4', 'btn']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela')

        self.var1 = tk.IntVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.IntVar()

        self.cb1 = tk.Checkbutton(self.nossaTela, text='Check 1', variable=self.var1,
                                  command=self.mudanca)
        self.cb1.place(x=50, y=50)

        self.cb2 = tk.Checkbutton(self.nossaTela, text='Check 2', variable=self.var2)
        self.cb2.place(x=50, y=70)
        self.cb2.select()

        self.cb3 = tk.Checkbutton(self.nossaTela, text='Check 3', variable=self.var3,
                                  offvalue='Não Selecionado', onvalue='Selecionado')
        self.cb3.place(x=50, y=90)

        self.cb4 = tk.Checkbutton(self.nossaTela, text='Check 4', variable=self.var4)
        self.cb4.place(x=50, y=110)

        self.btn = tk.Button(self.nossaTela, text='Click Aqui', command=self.confirma)
        self.btn.place(x=50, y=150)

    def confirma(self):
        print(f'CheckButton 1: {self.var1.get()}\n'
              f'CheckButton 2: {self.var2.get()}\n'
              f'CheckButton 3: {self.var3.get()}\n'
              f'CheckButton 4: {self.var4.get()}')

    def mudanca(self):
        print('Mudou o Estado')
        self.cb3['state'] = 'disable'


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
