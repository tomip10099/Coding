from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def boton():
    print("Boton presionado")

def window():

    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(800, 400, 300, 300)
    win.setWindowTitle("Test")

    label = QtWidgets.QLabel(win)
    label.setText("label")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click")
    b1.clicked.connect(boton)

    win.show()
    sys.exit(app.exec_())

window()