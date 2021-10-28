import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    """ APENAS DESIGN - VER CLASSE ABAIXO """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuAquivo = QtWidgets.QMenu(self.menuBar)
        self.menuAquivo.setObjectName("menuAquivo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuAquivo.addAction(self.actionAbrir)
        self.menuBar.addAction(self.menuAquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JANELA"))
        self.menuAquivo.setTitle(_translate("MainWindow", "Aquivo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))


# O CÓDIGO QUE VOCÊ QUER ESTÁ ABAIXO

class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Menu abrir
        self.menuAquivo.triggered.connect(self.troca_texto)

    def troca_texto(self):
        # Action
        self.menuAquivo.setTitle('IH, MUDEI O TITLE DO MENU!')
        self.actionAbrir.setText('IH, MUDEI O TEXTO DA ACTION ABRIR!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    qt.exec_()
