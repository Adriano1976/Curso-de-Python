"""
- QFileDialog.getOpenFileName retorna mais de uma coisa e eu estava interessado
apenas na primeira... o _ significa que eu não quero usar este valor...
- Exemplo: nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
- se eu quisesse, por exemplo, só a extensão do arquivo eu poderia colocar: _,
ext_arquivo = os.path.splitext(arquivo). Isso me retornaria apenas a extensão?
 Sim, mas isso não elimina o valor de _, é apenas uma conversão que usamos...
- Pra indicar para outros desenvolvedores que não vamos usar o _.
- "QMainWindow" foi criado com base nas necessidades de uma janela principal.
Por exemplo, tem locais para barra de menus, barra de status, barra de ferramentas
e assim por diante. Tudo que uma janela principal precisa.
- A "QWidget" já é a base de todas as classes que são desenhadas pelo QT.
- Você vai usar QMainWindow quando quiser uma janela principal e QWidget quando
quiser qualquer outro Widget.
"""

import sys
import design
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)  # Acionando método
        self.btnRedimencionar.clicked.connect(self.redimensionar)  # Acionando método
        self.btnSalvar.clicked.connect(self.salvar)  # Acionando método

    def abrir_imagem(self):  # Método abrir imagem
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralWidget(),
            'Abrir imagem',
            r'/Users/ADRIANO/Imagens/',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):  # método redimensionar imagem
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):  # Método salvar imagem
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralWidget(),
            'Salvar imagem',
            r'/Users/ADRIANO/Imagens/',
            '*.png'
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
