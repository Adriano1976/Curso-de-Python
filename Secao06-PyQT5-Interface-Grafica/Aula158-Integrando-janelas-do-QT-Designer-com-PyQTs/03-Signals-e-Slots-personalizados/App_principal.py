import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import *


class Sinais(QtCore.QObject):
    sinal1 = QtCore.pyqtSignal()
    sinal2 = QtCore.pyqtSignal(str, name='sinalStr')


class Tela(QMainWindow):  # Acessa funcionalidades da super classe.
    def __init__(self):
        super().__init__()
        self.ui = Ui_Interface()  # Instanciando a super classe.
        self.ui.setupUi(self)  # Chamando a super classe.
        self.sinais = Sinais()

        # self.objeto.signal.connect(self.slot)
        self.ui.btn.clicked.connect(self.funcao)

    @QtCore.pyqtSlot()
    def funcao(self):
        print('Botão clicado.')
        self.sinais.sinal1.connect((self.recebeSinal1))
        self.sinais.sinal1.emit()
        self.sinais.sinal1.disconnect()
        self.sinais.sinal2.connect((self.recebeSinal2))
        self.sinais.sinal2.emit('Sinal 2 enviado.')
        self.sinais.sinal2.disconnect()

    @QtCore.pyqtSlot()
    def recebeSinal1(self):
        print('Sinal 1 emitido com sucesso.')

    @QtCore.pyqtSlot(str)
    def recebeSinal2(self, valor):
        print(valor)


if __name__ == "__main__":  # Vefifica se o código está sendo executado diretamente ou não.
    app = QApplication(sys.argv)  # Criando um objeto da aplicação.
    w = Tela()  # Criando uma instância.
    w.show()  # Alocar o código na memória e mostrar na tela ao usuário.
    sys.exit(app.exec_())  # Garante que a janela aparece ao usuário até que seja feixado.
