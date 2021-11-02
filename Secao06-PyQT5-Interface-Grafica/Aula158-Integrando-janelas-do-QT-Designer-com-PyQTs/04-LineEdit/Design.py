# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ADRIANO\Desktop\Design.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditInput_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput_1.setGeometry(QtCore.QRect(30, 70, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditInput_1.setFont(font)
        self.lineEditInput_1.setText("")
        self.lineEditInput_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput_1.setDragEnabled(False)
        self.lineEditInput_1.setClearButtonEnabled(True)
        self.lineEditInput_1.setObjectName("lineEditInput_1")
        self.lineEditOutput_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutput_1.setGeometry(QtCore.QRect(30, 210, 161, 20))
        self.lineEditOutput_1.setObjectName("lineEditOutput_1")
        self.lineEditOutput_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutput_2.setGeometry(QtCore.QRect(220, 210, 111, 20))
        self.lineEditOutput_2.setObjectName("lineEditOutput_2")
        self.lineEditInput_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput_2.setGeometry(QtCore.QRect(220, 70, 111, 20))
        self.lineEditInput_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput_2.setClearButtonEnabled(True)
        self.lineEditInput_2.setObjectName("lineEditInput_2")
        self.pushButtonEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(280, 270, 141, 31))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.lineEditInput_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput_3.setGeometry(QtCore.QRect(362, 70, 131, 20))
        self.lineEditInput_3.setText("")
        self.lineEditInput_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput_3.setClearButtonEnabled(True)
        self.lineEditInput_3.setObjectName("lineEditInput_3")
        self.lineEditInput_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput_4.setGeometry(QtCore.QRect(522, 70, 131, 20))
        self.lineEditInput_4.setInputMask("")
        self.lineEditInput_4.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditInput_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput_4.setClearButtonEnabled(True)
        self.lineEditInput_4.setObjectName("lineEditInput_4")
        self.lineEditOutput_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutput_3.setGeometry(QtCore.QRect(362, 210, 131, 20))
        self.lineEditOutput_3.setObjectName("lineEditOutput_3")
        self.lineEditOutput_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOutput_4.setGeometry(QtCore.QRect(522, 210, 131, 20))
        self.lineEditOutput_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditOutput_4.setObjectName("lineEditOutput_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 160, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 130, 671, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEditInput_1.setInputMask(_translate("MainWindow", "aaaaaaaaaaaaaaa"))
        self.lineEditInput_1.setPlaceholderText(_translate("MainWindow", "Nome Completo"))
        self.lineEditOutput_1.setInputMask(_translate("MainWindow", "aaaaaaaaaaaaaaaaaaaa"))
        self.lineEditOutput_2.setInputMask(_translate("MainWindow", ">NNN.NNN.NNN-NN"))
        self.lineEditInput_2.setInputMask(_translate("MainWindow", ">NNNNNNNNNNN"))
        self.lineEditInput_2.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.pushButtonEnviar.setText(_translate("MainWindow", "Enviar"))
        self.lineEditInput_3.setInputMask(_translate("MainWindow", "NNNNNNNNNNN"))
        self.lineEditInput_3.setPlaceholderText(_translate("MainWindow", "Telefone"))
        self.lineEditInput_4.setPlaceholderText(_translate("MainWindow", "Senha com 8 dígitos"))
        self.lineEditOutput_3.setInputMask(_translate("MainWindow", "<\\[NN\\]NNNNN-NNNN"))
        self.label.setText(_translate("MainWindow", "Entrada de Dados"))
        self.label_2.setText(_translate("MainWindow", "Saida de Dados"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())