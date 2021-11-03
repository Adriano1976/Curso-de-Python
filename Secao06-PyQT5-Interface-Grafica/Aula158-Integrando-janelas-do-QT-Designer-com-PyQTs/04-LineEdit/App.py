import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Design import *


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.objeto.signal.connect(self.slot)
        self.ui.pushButtonEnviar.clicked.connect(self.enviar)
        self.ui.pushButtonLimpar.clicked.connect(self.limpar)

    def enviar(self):
        self.ui.lineEditOutput_1.setText(self.ui.lineEditInput_1.text())
        self.ui.lineEditOutput_2.setText(self.ui.lineEditInput_2.text())
        self.ui.lineEditOutput_3.setText(self.ui.lineEditInput_3.text())
        self.ui.lineEditOutput_4.setText(self.ui.lineEditInput_4.text())

    def limpar(self):
        self.ui.lineEditInput_1.clear()
        self.ui.lineEditInput_2.clear()
        self.ui.lineEditInput_3.clear()
        self.ui.lineEditInput_4.clear()
        self.ui.lineEditOutput_1.clear()
        self.ui.lineEditOutput_2.clear()
        self.ui.lineEditOutput_3.clear()
        self.ui.lineEditOutput_4.clear()


if __name__ == '__main__':
    applic = QApplication(sys.argv)
    app = App()
    app.show()
    applic.exec_()
