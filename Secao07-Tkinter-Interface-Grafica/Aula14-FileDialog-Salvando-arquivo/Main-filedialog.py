import tkinter as tk
from tkinter import filedialog


class Tela:
    __slots__ = ['nossaTela', 'barra_menu', 'arquivo1', 'arquivo2']

    def __init__(self, master):
        # Construction of object
        self.arquivo1 = None
        self.arquivo2 = None
        self.nossaTela = master
        self.barra_menu = tk.Menu(self.nossaTela)

        # Startup and configuration of objects principals
        self.nossaTela.title('Janela Principal')
        self.nossaTela.config(menu=self.barra_menu)

        # Startup and configuration of principal "barra_menu"
        self.barra_menu.add_command(label='Salvar', command=self.salvar)
        self.barra_menu.add_command(label='Salvar no diretório...', command=self.salvarNoDiretorio)

    # Create method "Salvar"
    def salvar(self):
        self.arquivo1 = filedialog.asksaveasfile(
            mode='w', defaultextension='.txt',
            filetypes=(
                ('Arquivo Python', '*.py'),
                ('Arquivo de Texto', '*.txt'))
        )

        if self.arquivo1 is not None:
            print('Arquivo foi criado')

            self.arquivo1.write("print('Olá Mundo!')")
            self.arquivo1.close()
        else:
            print('Erro')

    def salvarNoDiretorio(self):
        self.arquivo2 = filedialog.asksaveasfilename(
            defaultextension='.txt',
            initialdir=r'C:\Users\ADRIANO\Área de Trabalho'
        )

        if self.arquivo2 is not None:
            print(self.arquivo2)

            self.arquivo2.write("print('Olá Mundo!')")
            self.arquivo2.close()
        else:
            print('Erro')


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
