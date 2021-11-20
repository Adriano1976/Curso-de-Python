import tkinter as tk


class Janela2:
    __slots__ = ['nova', 'origem', 'btn']

    def __init__(self, master, root):
        self.nova = master
        self.nova.title('Janela Secundária')

        self.origem = root

        self.btn = tk.Button(self.nova, text='Abrir interface', bg='FireBrick', fg='white', width=18, height=3,
                             command=self.voltar)
        self.btn['font'] = ('Arial', '12')
        self.btn.pack(padx=100, pady=50)

    def voltar(self):
        self.origem.deiconify()
        self.nova.destroy()


class Tela:
    __slots__ = ['nossaTela', 'btn', 'novaTela']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela Principal')

        self.novaTela = None

        self.btn = tk.Button(self.nossaTela, text='Abrir interface', background='OliveDrab',
                             fg='white', width=18, height=3, command=self.abrir)
        self.btn['font'] = ('Arial', '12')
        self.btn.pack(padx=100, pady=50)

    def abrir(self):
        self.nossaTela.withdraw()
        self.novaTela = tk.Toplevel(self.nossaTela)
        Janela2(self.novaTela, self.nossaTela)


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
