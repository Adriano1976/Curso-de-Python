import tkinter as tk


class Tela:
    __slots__ = ['master', 'btn1', 'btn2', 'btn3', 'btn4']

    def __init__(self, master):
        self.master = master
        self.master.title('Janela Principal')

        self.btn1 = tk.Button(self.master, text='Botão 1', font=('Verdana', '13'), background='red')
        self.btn1.grid(row=0, column=0)

        self.btn2 = tk.Button(self.master, text='Botão 2', font=('Verdana', '13'), background='yellow')
        self.btn2.grid(row=0, column=1)

        self.btn3 = tk.Button(self.master, text='Botão 3', font=('Verdana', '13'), background='green')
        self.btn3.grid(row=2, column=0)

        self.btn4 = tk.Button(self.master, text='Botão 4', font=('Verdana', '13'), background='orange')
        self.btn4.grid(row=2, column=3, columnspan=2)


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
