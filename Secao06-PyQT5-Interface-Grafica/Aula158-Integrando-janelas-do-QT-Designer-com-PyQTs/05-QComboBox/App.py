import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import *


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.object.signal.connect(self.slot)
        self.ui.pushButtonSalvar.clicked.connect(self.enviar)

    @QtCore.pyqtSlot()
    def enviar(self):
        self.ui.lineEditOutputMateria.setText(self.ui.lineEditInputMateria.text())
        self.ui.lineEditOutputNota.setText(self.ui.lineEditInputNota.text())
        self.ui.label_3.setText('Salvo com sucesso!')


if __name__ == '__main__':
    applic = QApplication(sys.argv)
    app = App()
    app.show()
    applic.exec_()
