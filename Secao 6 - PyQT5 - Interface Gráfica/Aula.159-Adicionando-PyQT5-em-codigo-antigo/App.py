import sys
from Valida_cpf_001 import validar_cpf
from Gera_cpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow

import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnValidaCPF.clicked.connect(self.valida_cpf)
        self.btnGeraCPF.clicked.connect(self.gera_cpf)

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(validar_cpf(cpf))
        )

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
