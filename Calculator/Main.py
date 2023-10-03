#Main program
from GUI_v01 import *
import Calculo_de_ejes
import Secciones
import Fatiga
import sys

def calcular_ejes():

    caso = ui.Caso_comboBox.currentText() #Almacena string de caso
    check_coeficiente_seguridad = ui.coeficiente_seguridad_checkBox.isChecked() #Almacena True or False
    coeficiente_seguridad = ui.Coeficiente_seguridad_lineEdit.text() #Almacena un numero

    #Calculo de los valores geometricos del eje
    seccion =  ui.seccion_comboBox.currentText() #Almacena string de la seccion
    medida_representativa_1 = ui.Diametro_input_lineEdit.text() #Almacena numero de diametro
    medida_representativa_2 = 0
    longitud = ui.Longitud_input_lineEdit.text() #Almacena numero de longitud
    vel_giro = ui.velocidad_giro_input_lineEdit.text() #Almacena numero de velocidad de giro
    #ui.Momento_inercia_axial_input_lineEdit
    #ui.Momento_inercia_polar_input_lineEdit
    
    area, second_moment_area, second_moment_torsion, longitud, vel_giro = Calculo_de_ejes.geometria(seccion, float(medida_representativa_1), float(medida_representativa_2), float(longitud), float(vel_giro))

    #Calculo de esfuerzos y concentracion de tensiones del eje
    momento_alterno_flexion = ui.mom_alt_flex_lineEdit.text()
    momento_medio_flexion = ui.mom_med_flex_lineEdit.text()
    torsion_alterna = ui.torsion_alt_lineEdit.text()
    torsion_media = ui.torsion_media_lineEdit.text()

    check_concentracion_tensiones = ui.Concentracion_tensiones_checkBox.isChecked()
    tipo_concentracion_tensiones = ui.tipo_concentracion_tension_comboBox.currentText()
    factor_kf = ui.Factor_kf_lineEdit.text()
    factor_kfs = ui.Factor_kfs_lineEdit.text()
    #ui.concentracion_tensiones_pushButton.clicked.connect()

    tension_alterna, tension_media = Calculo_de_ejes.esfuerzos(float(momento_alterno_flexion), float(momento_medio_flexion), float(torsion_alterna), float(torsion_media), float(factor_kf), float(factor_kfs), float(medida_representativa_1), float(second_moment_area), float(second_moment_torsion))

    #Calculo de variables del material
    tipo_material = ui.Tipo_Material_comboBox.currentText()
    norma_material = ui.Norma_material_comboBox.currentText()
    proceso_fabricacion = ui.Proceso_fabricacion_comboBox.currentText()
    codigo_material = ui.Codigo_material_lineEdit.text()

    check_dureza_personalizada = ui.Dureza_perzonalizada_checkBox.isChecked()
    dureza = ui.Dureza_lineEdit.text() 
    tipo_dureza = ui.Dureza_comboBox.currentText()

    check_tratamiento_termico = ui.Trat_termico_checkBox.isChecked()
    tipo_tratamiento_termico = ui.Tipo_tratamiento_termico_comboBox.currentText()

    Su, Sy, Hb = Calculo_de_ejes.material(tipo_material, norma_material, codigo_material, proceso_fabricacion, check_dureza_personalizada, float(dureza), tipo_dureza, check_tratamiento_termico, tipo_tratamiento_termico)

    # tension_fluencia = ui.Tension_fluencia_lineEdit.text()
    # tension_ultima = ui.Tension_ultima_lineEdit.text()

    #Calculo de tension limite de fatiga
    Se = Fatiga.tension_fatiga(Su, True, float(medida_representativa_1))
    #Calculo de diametros minimos
    d_goodman, d_gerber, d_soderberg, d_ASME = Calculo_de_ejes.diametros_minimos(Se, Su, Sy, float(momento_medio_flexion), float(momento_alterno_flexion), float(torsion_media), float(torsion_alterna), float(coeficiente_seguridad), float(factor_kf), float(factor_kfs))

    #Calculo de coeficientes de seguridad
    n_soderberg,n_goodman,n_gerber,n_ASME,n_Langer =Calculo_de_ejes.coeficientes_seguridad(Se, Su, Sy, tension_alterna, tension_media)

    #line_edit.textChanged.connect(lambda text: button.setEnabled(len(text) > 0))
    print("Diametros: \n", round(d_goodman), " \n", round(d_gerber), " \n", round(d_soderberg), " \n", round(d_ASME),"\n")
    print("Coeficientes de seguridad: \n", round(n_goodman), " \n", round(n_gerber), " \n", round(n_soderberg), " \n", round(n_ASME)," \n", round(n_Langer))
    print("Calculo finalizado")

def modulos_ejes():
    #Al presionar el boton CALCULAR en el modulo de ejes se obtienen los datos almacenados
    ui.Calcular_pushButton.clicked.connect(lambda: calcular_ejes())


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

