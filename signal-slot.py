import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QPlainTextEdit, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Slot, Signal


class TestWin(QMainWindow):
    squareSignal = Signal()
    cubeSignal = Signal()

    def __init__(self):
        super().__init__()
        self.win = QMainWindow()
        self.win.setWindowIcon(QIcon('tu04.png'))
        self.win.resize(700, 600)
        self.win.move(600, 250)
        self.win.setWindowTitle('简易计算器')
        self.win.setStyleSheet('''font-size:30px; font-weight:bolder''')

        self.lable1 = QLabel(self.win)
        self.lable1.setText('''number:''')
        # self.lable1.setStyleSheet('''font-color:#0002ff''')
        self.lable1.move(100, 100)
        # self.lable1.setStyleSheet('''font-size:20px''')

        self.eidt = QLineEdit(self.win)
        self.eidt.move(220, 85)
        self.eidt.resize(150, 50)
        self.eidt.setText('0')

        #square
        self.tEdit1 = QPlainTextEdit(self.win)
        self.tEdit1.setPlainText("NULL")
        self.tEdit1.move(360, 225)
        self.tEdit1.resize(150, 50)
        self.tbutton1 = QPushButton('平方(直接触发)', self.win)
        self.tbutton1.setStyleSheet('''background-color:#00ff00''')
        self.tbutton1.move(100, 200)
        self.tbutton1.resize(250, 50)
        self.tbutton2 = QPushButton('平方(信号槽触发)', self.win)
        self.tbutton2.setStyleSheet('''background-color:#aaff00''')
        self.tbutton2.move(100, 260)
        self.tbutton2.resize(250, 50)

        #cube
        self.tEdit2 = QPlainTextEdit(self.win)
        self.tEdit2.setPlainText("NULL")
        self.tEdit2.resize(150, 50)
        self.tEdit2.move(360, 425)
        self.tbutton3 = QPushButton("立方(直接触发)", self.win)
        self.tbutton3.setStyleSheet('''background-color:#fd1254''')
        self.tbutton3.resize(250, 50)
        self.tbutton3.move(100, 400)
        self.tbutton4 = QPushButton('立方(信号槽触发)', self.win)
        self.tbutton4.setStyleSheet('''background-color:#ccffcc''')
        self.tbutton4.move(100, 460)
        self.tbutton4.resize(250, 50)

        #
        self.tbutton5 = QPushButton('归零', self.win)
        self.tbutton5.setStyleSheet('''background-color:#ff33cc''')
        self.tbutton5.resize(100, 50)
        self.tbutton5.move(400, 85)

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.tbutton1)
        # self.layout.addWidget(self.tbutton2)
        # self.win.setLayout(self.layout)
        # self.layout2 = QHBoxLayout()
        # self.layout2.addWidget(self.tbutton1)
        # self.layout2.addWidget(self.tbutton2)
        # self.win.setLayout(self.layout2)

        #connect
        self.tbutton1.clicked.connect(self.ShowSquare)
        self.tbutton3.clicked.connect(self.ShowCube)
        self.tbutton2.clicked.connect(self.SquareSignalEmit)
        self.tbutton4.clicked.connect(self.CubeSignalEmit)
        self.tbutton5.clicked.connect(self.SetZero)
        self.squareSignal.connect(self.ShowSquare)
        self.cubeSignal.connect(self.ShowCube)


    # def handleClicked(self):
    #     self.tEdit1.setPlainText('Clicked')
    #     QMessageBox.about(self.win, 'Message', 'Button Clicked')

    def SquareSignalEmit(self):
        self.squareSignal.emit()
        # pass

    def CubeSignalEmit(self):
        self.cubeSignal.emit()

    def ShowSquare(self):
        self.tEdit1.setPlainText(str(int(self.eidt.text()) * int(self.eidt.text())))

    def ShowCube(self):
        self.tEdit2.setPlainText(str(int(self.eidt.text()) * int(self.eidt.text()) * int(self.eidt.text())))

    def SetZero(self):
        self.eidt.setText('0')
        self.tEdit1.setPlainText('0')
        self.tEdit2.setPlainText('0')

if __name__ == '__main__':
    app = QApplication()
    twin = TestWin()
    twin.win.show()
    # twin.test()
    app.exec_()
