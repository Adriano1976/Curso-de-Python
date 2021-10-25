"""
- PyQT é um toolkit desenvolvido em C++ utilizado por vários programadores para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...
- pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.setStyleSheet('font-size: 20px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        # Dessa forma a saída é no terminal, caso a ação
        # seja mais complexa, deve-se jogar em um método
        self.btn.clicked.connect(lambda: print('Olá mundo!'))

        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()

    app.show()
    qt.exec_()
