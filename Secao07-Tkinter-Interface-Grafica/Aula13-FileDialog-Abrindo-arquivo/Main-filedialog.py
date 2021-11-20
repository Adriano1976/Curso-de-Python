import tkinter as tk
from tkinter import filedialog


class Tela:
    __slots__ = ['nossaTela', 'barra_menu', 'arquivo1', 'arquivo2', 'conteudo']

    def __init__(self, master):
        # Construction of object
        self.arquivo1 = None
        self.arquivo2 = None
        self.conteudo = None
        self.nossaTela = master
        self.barra_menu = tk.Menu(self.nossaTela)

        # Startup and configuration of objects principals
        self.nossaTela.title('Janela Principal')
        self.nossaTela.config(menu=self.barra_menu)

        # Startup and configuration of principal "barra_menu"
        self.barra_menu.add_command(label='Ler arquivo', command=self.lerArquivo)
        self.barra_menu.add_command(label='Abrir diretório do arquivo', command=self.abrirDir)

    # Create method "lerArquivo"
    def lerArquivo(self):
        self.arquivo1 = filedialog.askopenfile(mode='r',
                                               initialdir=r'\Desktop',
                                               title='Selecione um arquivo',
                                               filetypes=(('Arquivos de texto', '*.txt'),
                                                          ('Arquivo Python', '*.py')))

        self.conteudo = self.arquivo1.read()
        print(self.conteudo)
        self.arquivo1.close()

    def abrirDir(self):
        self.arquivo2 = filedialog.askopenfilename(initialdir=r'\Desktop',
                                                   title='Selecione um arquivo',
                                                   filetypes=(('Arquivos de texto', '*.txt'),
                                                              ('Arquivo Python', '*.py')),
                                                   initialfile='Atividade 2.txt')

        print(self.arquivo2)


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
