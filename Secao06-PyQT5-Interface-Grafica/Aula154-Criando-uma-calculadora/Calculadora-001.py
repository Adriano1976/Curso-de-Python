"""
- O '__slots__' avisa o Python para não usar um dicionário e apenas aloçar espaço
para um conjunto fixo de atributos.
- Muitos programadores viram uma redução de quase 40 a 50% do uso de RAM usando essa
técnica.
- As funções lambda são somente um trecho de código anônimo que facilita a vida
do desenvolvedor, porque ao invés de criar uma função completa pra fazer determinada
ação, criamos as funções anônimas com uma linha (mais curta).
- "eval" é uma função que avalia um texto e tenta interpretá-lo como código...
então se eu envio uma string como "2 + 2", eval avalia isso como código Python,
gerando 4.
- O comando "qt.exec_()"  inicia o event loop (um loop que verifica eventos que ocorrem na janela). Quando você
clica em botões, a ação de clicar dispara um evento que chama a função desejada.

001 - Muda o título a 00-Interface;
002 - Coloca um tamanho fixo da janela da 00-Interface;
003 - Adicionando um grid na 00-Interface;
004 - Criação do display da calculadora;
005 - Adiciona o display da calculadora no grid;
006 - Desabilita a opção do usuário digitar no display da calculadora;
007 - Definição do estilo calculadora;
008 - Faz o display expandir para o topo;
009 - Criação de um widget principal;
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    __slots__ = ['cw', 'grid', 'display']

    def __init__(self, parent=None):
        super().__init__(parent)

        # Janela da calculadora
        self.setWindowTitle('Calculadora')  # 001
        self.setFixedSize(400, 400)  # 002
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)  # 003

        # Display da calculadora
        self.display = QLineEdit()  # 004
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # 005
        self.display.setDisabled(True)  # 006
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'  # 007
        )

        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )  # 008

        # Adição dos botões numéricos e operações da calculadora na linha 1
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #d5580d; color: #fff; font-weight:700;'
        )

        # Adição dos botões numéricos e operações da calculadora na linha 2
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            )
        )

        # Adição dos botões numéricos e operações da calculadora na linha 3
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        self.add_btn(QPushButton('%'), 3, 4, 1, 1)

        # Adição dos botões numéricos e operações da calculadora na linha 4
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('00'), 4, 2, 1, 1)
        self.add_btn(QPushButton('/'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #095177; color: #fff; font-weight:700;'
        )

        self.setCentralWidget(self.cw)  # 009

    # Designer e funcionalidade dos botões
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()

    calc.show()
    qt.exec_()
