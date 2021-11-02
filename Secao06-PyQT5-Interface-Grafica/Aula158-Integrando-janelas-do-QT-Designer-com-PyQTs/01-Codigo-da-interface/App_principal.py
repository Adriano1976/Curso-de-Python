import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import *


class Tela(QMainWindow):  # Acessa funcionalidades da super classe.
    def __init__(self):
        super().__init__()
        self.ui = Ui_Interface()  # Instanciando a super classe.
        self.ui.setupUi(self)  # Chamando a super classe.


if __name__ == "__main__":  # Vefifica se o código está sendo executado diretamente ou não.
    app = QApplication(sys.argv)  # Criando um objeto da aplicação.
    w = Tela()  # Criando uma instância.
    w.show()  # Alocar o código na memória e mostrar na tela ao usuário.
    sys.exit(app.exec_())  # Garante que a janela aparece ao usuário até que seja feixado.
