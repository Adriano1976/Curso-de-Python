import tkinter as tk
from tkinter import messagebox


class Tela:
    __slots__ = ['nossaTela', 'btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn8',
                 'caixa1', 'caixa2', 'caixa3', 'caixa4', 'caixa5', 'caixa6', 'caixa7', 'caixa8']

    def __init__(self, master):
        self.nossaTela = master

        self.btn1 = tk.Button(self.nossaTela, text='Botão 1', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas1)
        self.btn2 = tk.Button(self.nossaTela, text='Botão 2', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas2)
        self.btn3 = tk.Button(self.nossaTela, text='Botão 3', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas3)
        self.btn4 = tk.Button(self.nossaTela, text='Botão 4', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas4)
        self.btn5 = tk.Button(self.nossaTela, text='Botão 5', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas5)
        self.btn6 = tk.Button(self.nossaTela, text='Botão 6', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas6)
        self.btn7 = tk.Button(self.nossaTela, text='Botão 7', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas7)
        self.btn8 = tk.Button(self.nossaTela, text='Botão 8', bg='FireBrick', fg='white', width=18, height=3, command=self.caixas8)

        self.caixa1 = None
        self.caixa2 = None
        self.caixa3 = None
        self.caixa4 = None
        self.caixa5 = None
        self.caixa6 = None
        self.caixa7 = None
        self.caixa8 = None

        self.nossaTela.title('Janela Principal')
        self.btn1.pack(padx=100, pady=10)
        self.btn2.pack(padx=100, pady=10)
        self.btn3.pack(padx=100, pady=10)
        self.btn4.pack(padx=100, pady=10)
        self.btn5.pack(padx=100, pady=10)
        self.btn6.pack(padx=100, pady=10)
        self.btn7.pack(padx=100, pady=10)
        self.btn8.pack(padx=100, pady=10)

    # Other function with show: showinfo, showwarning, showerror.
    # Other function with ask: askquestion, askokcancel, askretrycancel, askyesno, askyesnocancel.

    def caixas1(self):
        self.caixa1 = messagebox.showinfo('Informação', 'Realmente temos uma informação do Botão 1')
        print(self.caixa1)
        if self.caixa1 == 'ok':
            print('Escolha Certa!')

    def caixas2(self):
        self.caixa2 = messagebox.showwarning('Informação', 'Realmente temos uma informação do Botão 2')
        print(self.caixa2)
        if self.caixa2 == 'ok':
            print('Escolha certa!')

    def caixas3(self):
        self.caixa3 = messagebox.showerror('Informação', 'Realmente temos uma informação do Botão 3')
        print(self.caixa3)
        if self.caixa3 == 'ok':
            print('Escolha certa!')

    def caixas4(self):
        self.caixa4 = messagebox.askquestion('Informação', 'Realmente temos uma informação do Botão 4')
        print(self.caixa4)
        if self.caixa4 == 'yes':
            print('Escolha certa!')
        else:
            print('Escolha Errada!')

    def caixas5(self):
        self.caixa5 = messagebox.askokcancel('Informação', 'Realmente temos uma informação do Botão 5')
        print(self.caixa5)
        if self.caixa5:
            print('Escolha certa!')
        else:
            print('Escolha Errada!')

    def caixas6(self):
        self.caixa6 = messagebox.askretrycancel('Informação', 'Realmente temos uma informação do Botão 6')
        print(self.caixa6)
        if self.caixa6:
            print('Escolha certa!')
        else:
            print('Escolha Errada1')

    def caixas7(self):
        self.caixa7 = messagebox.askyesno('Informação', 'Realmente temos uma informação do Botão 7')
        print(self.caixa7)
        if self.caixa7:
            print('Escolha certa!')
        else:
            print('Escolha Errada!')

    def caixas8(self):
        self.caixa8 = messagebox.askyesnocancel('Informação', 'Realmente temos uma informação do Botão 8')
        print(self.caixa8)
        if self.caixa8:
            print('Escolha certa!')
        else:
            print('Escolha Errada')


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
