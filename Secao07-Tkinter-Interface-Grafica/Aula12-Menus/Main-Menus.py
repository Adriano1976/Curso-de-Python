import tkinter as tk


class Tela:
    __slots__ = ['nossaTela', 'barra_menu', 'arquivo', 'abrir']

    def __init__(self, master):
        # Construction of object
        self.nossaTela = master
        self.barra_menu = tk.Menu(self.nossaTela)
        self.arquivo = tk.Menu(self.barra_menu, tearoff=0)
        self.abrir = tk.Menu(self.arquivo, tearoff=0)

        # Startup and configuration of object principal "nossaTesla"
        self.nossaTela.title('Janela')
        self.nossaTela.config(menu=self.barra_menu)

        # Startup and configuration of principal "barra_menu"
        self.barra_menu.add_cascade(label='Arquivo', menu=self.arquivo)
        self.barra_menu.add_command(label='Editar')
        self.barra_menu.add_command(label='Ajuda')

        # Startup and configuration of submenu principal "arquivo"
        self.arquivo.add_command(label='Novo')
        self.arquivo.add_separator()
        self.arquivo.add_cascade(label='Abrir', menu=self.abrir)
        self.arquivo.add_command(label='Salvar')
        self.arquivo.add_command(label='Editar')
        self.arquivo.add_command(label='Excluir')

        # Startup and configuration of submenu "abrir"
        self.abrir.add_command(label='Curso de Python')
        self.abrir.add_command(label='Curso de JavaScript')
        self.abrir.add_command(label='Curso de C++')
        self.abrir.add_command(label='Curso de Ruby')
        self.abrir.add_command(label='Curso de SQL')
        self.abrir.add_command(label='Curso de Linux')
        self.abrir.add_command(label='Curso de Lógica')


if __name__ == '__main__':
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
