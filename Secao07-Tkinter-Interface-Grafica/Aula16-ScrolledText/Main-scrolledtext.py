import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox


class Tela:
    __slots__ = ['nossaTela', 'txtArea', 'btn1', 'btn2', 'arquivo1', 'arquivo2', 'texto', 'conteudo',
                 'msgConfirm', 'msgErro', 'btn3', 'btnBusca', 'entry', 'msg']

    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title('Bloco de Notas')

        self.texto = None
        self.conteudo = None
        self.arquivo1 = None
        self.arquivo2 = None
        self.msgConfirm = None
        self.msgErro = None
        self.txtArea = None
        self.msg = None

        self.txtArea = scrolledtext.ScrolledText(self.nossaTela, wrap=tk.WORD)
        self.txtArea['font'] = ('Verdana', '11')
        self.txtArea.pack(expand=True, fill=tk.X)

        self.btn1 = tk.Button(self.nossaTela, text='Limpar', command=self.limpar, bg='FireBrick', fg='white', width=18, height=3)
        self.btn1['font'] = ('Verdana', '11')
        self.btn1.pack(side=tk.LEFT, pady=10, padx=10)

        self.btn2 = tk.Button(self.nossaTela, text='Salvar', command=self.salvar, bg='FireBrick', fg='white', width=18, height=3)
        self.btn2['font'] = ('Verdana', '11')
        self.btn2.pack(side=tk.LEFT, pady=10)

        self.btn2 = tk.Button(self.nossaTela, text='Abrir', command=self.abrir, bg='FireBrick', fg='white', width=18, height=3)
        self.btn2['font'] = ('Verdana', '11')
        self.btn2.pack(side=tk.LEFT, pady=10, padx=10)

        self.btnBusca = tk.Button(self.nossaTela, text='Buscar', command=self.buscar, bg='FireBrick', fg='white', width=18, height=3)
        self.btnBusca['font'] = ('Verdana', '11')
        self.btnBusca.pack(side=tk.LEFT, pady=10)

        self.entry = tk.Entry(self.nossaTela)
        self.entry['font'] = ('Verdana', '11')
        self.entry.pack(side=tk.LEFT, pady=10, padx=10)

    def limpar(self):
        self.txtArea.delete('1.0', tk.END)

    def salvar(self):
        self.texto = self.txtArea.get('1.0', tk.END)
        self.arquivo1 = filedialog.asksaveasfile(
            mode='w', defaultextension='.txt',
            filetypes=(
                ('Arquivo de Texto', '*.txt'),
                ('Arquivo em Python', '*.py')
            )
        )
        if self.arquivo1 is not None:
            self.arquivo1.write(self.texto)
            self.arquivo1.close()
            self.msgConfirm = messagebox.showinfo('Informação', 'Arquivo salvo com sucesso!')
        else:
            self.msgErro = messagebox.showwarning('Informação', 'Arquivo não foi salvo!')

    def abrir(self):

        self.arquivo2 = filedialog.askopenfiles(
            mode='w', defaultextension='.txt',
            filetypes=(
                ('Arquivo de Texto', '*.txt'),
                ('Arquivo em Python', '*.py'),
            )
        )
        self.txtArea.insert('1.0', self.arquivo2)

    def buscar(self):
        busca = self.entry.get()
        tamanho = len(busca)
        contador = 0
        comeco = '1.0'

        self.txtArea.tag_delete('encontrada')
        while True:
            pos = self.txtArea.search(pattern=busca, index=comeco, stopindex=tk.END, count=True)

            if not pos:
                self.msg = messagebox.showinfo('Informação', "Pesquisa finalizada"
                                                             ""f' {contador} localizado com: "{busca}"')
                break
            self.txtArea.tag_add('encontrada', pos, (pos + f'+{tamanho}c'))
            contador += 1
            comeco = pos + '+1c'

            self.txtArea.tag_config('encontrada', background='yellow')


if __name__ == '__main__':
    # Gerar a interface gráfica
    janelaRaiz = tk.Tk()
    Tela(janelaRaiz)
    janelaRaiz.mainloop()
