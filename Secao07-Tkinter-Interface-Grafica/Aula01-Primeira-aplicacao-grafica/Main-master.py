import tkinter as tk


class Tela:
    __slots__ = ['nossaTela']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela Principal')


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
