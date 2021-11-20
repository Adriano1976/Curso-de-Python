import tkinter as tk
from PIL import ImageTk, Image


class Tela:
    __slots__ = ['nossaTela', 'minhaImagem', 'lb1']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Janela Principal')

        img = Image.open(r'C:\Users\ADRIANO\Pictures\diagrama de caso uso.png')
        self.minhaImagem = ImageTk.PhotoImage(img)
        self.lb1 = tk.Label(self.nossaTela, image=self.minhaImagem)
        self.lb1.image = self.minhaImagem
        self.lb1.pack()


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
