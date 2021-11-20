import tkinter as tk


class Tela:
    __slots__ = ['master', 'btn1', 'btn2']

    def __init__(self, master):
        self.master = master
        self.master.title('Janela Principal')

        self.btn1 = tk.Button(self.master, text='Botão 1', font=('Verdana', '13'), background='pink')
        self.btn1.place(x=100, y=50, anchor=tk.CENTER)

        self.btn2 = tk.Button(self.master, text='Botão 2', font=('Arial', '15'), background='green')
        self.btn2.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.3)


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
