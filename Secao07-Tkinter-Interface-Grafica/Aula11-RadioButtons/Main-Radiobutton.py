import tkinter as tk


class Tela:
    __slots__ = ['nossaTela', 'cnt', 'lbl', 'rb1', 'rb2', 'rb3', 'rb4', 'rb5', 'btn']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela')

        # IntVar, StringVar ou BooleanVar
        self.cnt = tk.StringVar()

        self.lbl = tk.Label(self.nossaTela, text='Escolha o curso desejado:', background='orange')
        self.lbl['font'] = ('Verdana', '13')
        # self.lbl.grid(row=0, column=0)
        self.lbl.pack(padx=20, pady=20)

        self.rb1 = tk.Radiobutton(self.nossaTela, text='Python', variable=self.cnt,
                                  value='Curso em Python escolhido com sucesso!')
        self.rb1['font'] = ('Verdana', '10')
        self.rb1.pack(pady=5)
        self.rb1.select()
        # self.rb1.grid(row=1, column=0)

        self.rb2 = tk.Radiobutton(self.nossaTela, text='JavaScript', variable=self.cnt,
                                  value='Curso em JavaScript escolhido com sucesso!')
        self.rb2['font'] = ('Verdana', '10')
        # self.rb2.grid(row=2, column=0)
        self.rb2.pack(pady=5)

        self.rb3 = tk.Radiobutton(self.nossaTela, text='SQL', variable=self.cnt,
                                  value='Curso em SQL escolhido com sucesso!')
        self.rb3['font'] = ('Verdana', '10')
        # self.rb3.grid(row=3, column=0)
        self.rb3.pack(pady=5)

        self.rb4 = tk.Radiobutton(self.nossaTela, text='C++', variable=self.cnt,
                                  value='Curso em C++ escolhido com sucesso!')
        self.rb4['font'] = ('Verdana', '10')
        # self.rb4.grid(row=4, column=0)
        self.rb4.pack(pady=5)

        self.rb5 = tk.Radiobutton(self.nossaTela, text='Java', variable=self.cnt,
                                  value='Curso em Java escolhido com sucesso!')
        self.rb5['font'] = ('Verdana', '10')
        # self.rb5.grid(row=5, column=0)
        self.rb5.pack(pady=5)

        self.btn = tk.Button(self.nossaTela, text='Confirmar', command=self.func, background='red')
        self.btn['font'] = ('Verdana', '12')
        # self.btn.grid(row=6, column=0)
        self.btn.pack(pady=10, side=tk.BOTTOM)

    def func(self):
        print(self.cnt.get())


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
