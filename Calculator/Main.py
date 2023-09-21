#Main program

from GUI_v01 import *
from Calculo_de_ejes import *
import sys
import time

def get_data():
    caso = ui.Caso_comboBox.currentText()
    print(caso)

def modulos_ejes():
    #obtener datos almacenados
    caso = ui.Caso_comboBox.currentText()
    print(caso)

    #Al presionar el boton CALCULAR en el modulo de ejes se calcula todo el modulo
    ui.Calcular_pushButton.clicked.connect(lambda: get_data())


#Inicializar  el entorno grafico
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #Modulo calculo de ejes
    ui.Calculo_ejes_pushButton.clicked.connect(lambda: modulos_ejes())

    sys.exit(app.exec_())

