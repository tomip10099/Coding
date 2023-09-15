from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):

    def __init__(self):

        super(MyWindow, self).__init__()
        self.initUI()

        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle("Test")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.move(150,150)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.boton)

    def boton(self):
        self.label.setText("Boton presionado")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():

    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()