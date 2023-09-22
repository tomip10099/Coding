#Main program

from GUI_v01 import *
from Calculo_de_ejes import *
import sys
import time

def get_data_ejes():

    caso = ui.Caso_comboBox.currentText()
    check_coeficiente_seguridad = ui.coeficiente_seguridad_checkBox.isChecked()
    coeficiente_seguridad = ui.Coeficiente_seguridad_lineEdit.text()

    seccion =  ui.seccion_comboBox.currentText()
    diametro = ui.Diametro_input_lineEdit.text()
    longitud = ui.Longitud_input_lineEdit.text()
    vel_giro = ui.velocidad_giro_input_lineEdit.text()
    #ui.Momento_inercia_axial_input_lineEdit
    #ui.Momento_inercia_polar_input_lineEdit

    momento_alterno_flexion = ui.mom_alt_flex_lineEdit.text()
    momento_medio_flexion = ui.mom_med_flex_lineEdit.text()
    torsion_alterna = ui.torsion_alt_lineEdit.text()
    torsion_media = ui.torsion_media_lineEdit.text()

    tipo_material = ui.Tipo_Material_comboBox.currentText()
    norma_material = ui.Norma_material_comboBox.currentText()
    proceso_fabricacion = ui.Proceso_fabricacion_comboBox.currentText()

    check_dureza_personalizada = ui.Dureza_perzonalizada_checkBox.isChecked()
    dureza = ui.Dureza_lineEdit.text() 
    tipo_dureza = ui.Dureza_comboBox.currentText()

    check_tratamiento_termico = ui.Trat_termico_checkBox.isChecked()
    tipo_tratamiento_termico = ui.Tipo_tratamiento_termico_comboBox.currentText()

    tension_fluencia = ui.Tension_fluencia_lineEdit.text()
    tension_ultima = ui.Tension_ultima_lineEdit.text()

    check_concentracion_tensiones = ui.Concentracion_tensiones_checkBox.isChecked()
    tipo_concentracion_tensiones = ui.tipo_concentracion_tension_comboBox.currentText()
    factor_kf = ui.Factor_kf_lineEdit.text()
    factor_kft = ui.Factor_kft_lineEdit.text()
    #ui.concentracion_tensiones_pushButton.clicked.connect()


    #line_edit.textChanged.connect(lambda text: button.setEnabled(len(text) > 0))
    print("Calculo finalizado")


def modulos_ejes():
    #Al presionar el boton CALCULAR en el modulo de ejes se obtienen los datos almacenados
    ui.Calcular_pushButton.clicked.connect(lambda: get_data_ejes())


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

