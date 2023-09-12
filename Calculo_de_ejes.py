import numpy as np
import json
import Fatiga
import Secciones

############################################################################################
#Aclaraciones:

    #Shaft = Arbol
    #Axle = eje

    #En general los ejes se realizan de aceros con bajo carbono, SAE 1020 a 1050

    # Cuando los efectos de la resistencia resultand dominar la deflexiones se debe eligir un material de mayor resistencia, lo que permite 
    # reducir los tamaños del eje hasta que la deflexion resulte problematica.

    #Cuando es necesario tratamientos termicos o aceros aleados las opciones comunes son las siguientes: 1340/50 3140/50 4140 5140 8650
    #Ejes deformados en frio [cold drawn] se usan comunmnente para diametros menores a 3" = 76 mm

    #En general es mejor aplicar la carga en el eje en el espacio entre los rodamientos y no cargas en voladizo fuera de los rodamientos

    #Solo dos rodamientos debe ser usado en la mayoria de los casos, salvo casos de ejes muy largos(tener en cuenta la alineacion de los rodamientos con cuidado)

    #Por medio del analisis de Von Misses podemos combinar las diferentes tensiones, de flexion y torsion

    #Saf = Sigma a flexion = Tension alterna de flexion
    #Smf = Sigma m flexion = Tension media de flexion
    #Tat = Tao a Torsion = Tension alterna de torsion
    #Tmt = Tao m Torsion = Tension media de torsion 
    
###########################################################################################
#Parametros del problema

d = 30 #Diametro [mm]
Ma = 1 #Momento alterno de flexion [kg.mm]
Mm = 1 #Momento medio de flexion [kg.mm]
Ta = 1 #Torsion alterna [kg.mm]
Tm = 1 #Torsion media [kg.mm]
n = 1 #Coeficiente de seguridad
####################################################################################################

#Variables del material
with open("materialesSAE.json", "r") as file:
    materialesSAE = json.load(file)

material_name = "SAE 1006HR"


Su = materialesSAE[material_name]["Su"] #Tension ultima
Sy = materialesSAE[material_name]["Sy"] #Tension ultima
Se = Fatiga.tension_fatiga(Su, True, 30)
#####################################################################################################

#Concentracion de tensiones
kt = 1 #Factor de concentracion de tensiones teorico a flexion
kts = 1 #Factor de concentracion de tensiones teorico a torsion
r_e = 0 #radio de empalme

kf, _ = Fatiga.factor_concentracion_tensiones(kt, kts, r_e, Su) #Factor de concentracion de tensiones a flexion
_ , kfs = Fatiga.factor_concentracion_tensiones(kt, kts, r_e, Su)  #Factor de concentracion de tensiones a torsion

c = d/2 #Distancia a la fibra superior (en un circulo es el radio) [mm]
_ ,I, _ = Secciones.Circle(d) #Momento de inercia 2 orden respecto al eje de flexion, generalmente z [kg.mm4]
_, _, J = Secciones.Circle(d) #Momento de inercia 2 orden o polar respecto al eje de torsion, generalmente x [kg.mm4]
########################################################################################################

#Calculo de tensiones actuantes
saf_g = kf * (Ma * c / I )
smf_g = kf * (Mm * c / I )

tat_g = kfs * (Ta * c / J)
tmt_g = kfs * (Tm * c / J)

######################################################################################################

#Composicion de tensiones
sa = ((saf_g**2) + (3 * (tat_g**2)))**(1/2) #Sigma alterno
sm = ((smf_g**2) + (3 * (tmt_g**2)))**(1/2) #Sigma medio
###########################################################################################################


#Metodo de calculo por Goodman

d_goodman = (((16*n) / np.pi) * ((1/Se) * (((4 * ((kf * Ma)**2)) + (3 * ((kfs * Ta)**2)))**(1/2)) + (1/Su) * (((4 * ((kf * Mm)**2)) + (3 * ((kfs * Tm)**2)))**1/2)))**(1/3)  #[mm]

#Metodo de calculo por Gerber
A = ((4 * ((kf*Ma)**2)) + (3 * ((kfs * Ta)**2)))**1/2
B = ((4 * ((kf*Mm)**2)) + (3 * ((kfs * Tm)**2)))**1/2

d_gerber = (((8 * n * A) / (np.pi * Se)) * (1 + ((1 + (((2 * B * Se) / (A * Su))**2))**1/2)))**1/3 # [mm]

#Metodo de calculo ASME-Elliptic

d_ASME = (((16*n)/np.pi) * (((4*(((kf*Ma) / Se)**2)) + (3 * (((kfs * Ta) / Se)**2)) + (4 * (((kf*Mm) / Sy)**2)) + (3 * (((kfs * Tm) / Sy)**2)))**1/2))**1/3 # [mm]

#Metodo de calculo Soderberg

d_soderberg = ((16 * n / np.pi) * (((1/Se) * (((4 * ((kf*Ma)**2)) + (3 * ((kfs * Ta)**2)))**1/2)) + ((1/Sy) * (((4 * ((kf*Mm)**2)) + (3 * ((kfs * Tm)**2)))**1/2))))**1/3 # [mm]