import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Design import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioButton_2.setChecked(True)
        self.ui.radioButton_2.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_3.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_4.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_5.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_6.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_7.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_8.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_9.toggled.connect(self.mudancaDeEstado)
        self.ui.radioButton_10.toggled.connect(self.mudancaDeEstado)

        self.ui.pushButton.pressed.connect(self.salvar)
        self.ui.pushButton_2.pressed.connect(self.excluir)

    @QtCore.pyqtSlot()
    def mudancaDeEstado(self):
        radioSelecionado = self.sender()

        if radioSelecionado.isChecked():
            self.ui.lineEdit.setText(radioSelecionado.text())

    @QtCore.pyqtSlot()
    def salvar(self):
        self.ui.lineEdit.selectAll()
        self.ui.lineEdit.copy()
        self.ui.label_3.setText('Curso salvo com sucesso!')

    @QtCore.pyqtSlot()
    def excluir(self):
        self.ui.lineEdit.clear()
        self.ui.label_3.clear()


if __name__ == '__main__':
    applic = QApplication(sys.argv)
    app = App()
    app.show()
    applic.exec_()
