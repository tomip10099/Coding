import numpy as np

#Shaft = Arbol
#Axle = eje

#En general los ejes se realizan de aceros con bajo carbono, SAE 1020 a 1050

# Cuando los efectos de la resistencia resultand dominar la deflexiones se debe eligir un material de mayor resistencia, lo que permite 
#   reducir los tamaños del eje hasta que la deflexion resulte problematica.

#Cuando es necesario tratamientos termicos o aceros aleados las opciones comunes son las siguientes: 1340/50 3140/50 4140 5140 8650
#Ejes deformados en frio [cold drawn] se usan comunmnente para diametros menores a 3" = 76 mm

#En general es mejor aplicar la carga en el eje en el espacio entre los rodamientos y no cargas en voladizo fuera de los rodamientos

#Solo dos rodamientos debe ser usado en la mayoria de los casos, salvo casos de ejes muy largos(tener en cuenta la alineacion de los rodamientos con cuidado)


#Por medio del analisis de Von Misses podemos combinar las diferentes tensiones, de flexio y torsion

#Saf = Sigma a flexion = Tension alterna de flexion
#Smf = Sigma m flexion = Tension media de flexion
#Tat = Tao a Torsion = Tension alterna de torsion
#Tmt = Tao m Torsion = Tension media de torsion 

#Formulas generales (_g)

Ma = 1 #Momento alterno de flexion [kg.mm]
Mm = 1 #Momento medio de flexion [kg.mm]
Ta = 1 #Torsion alterna [kg.mm]
Tm = 1 #Torsion media [kg.mm]
kf = 1 #Factor de concentracion de tensiones a flexion
kfs = 1 #Factor de concentracion de tensiones a torsion
c = 1 #Distancia a la fibra superior (en un circulo es el radio) [mm]
I = 1 #Momento de inercia 2 orden respecto al eje de flexion, generalmente z [kg.mm4]
J = 1 #Momento de inercia 2 orden respecto al eje de torsion, generalmente x [kg.mm4]

saf_g = kf * (Ma * c / I )
smf_g = kf * (Mm * c / I )

tat_g = kfs * (Ta * c / J)
tmt_g = kfs * (Tm * c / J)

##########################################################################################

#Formulas para seccion circular llena (_sc)

d = 1 #diametro [mm]

saf_sc = kf * ((32 * Ma) / (np.pi * (d**3))) #Tension alterna de flexion
smf_sc = kf * ((32 * Mm) / (np.pi * (d**3))) #Tension media de flexion

tat_sc = kfs * ((16 * Ta) / (np.pi * (d**3))) #Tension alterna de torsion
tmt_sc = kfs * ((16 * Tm) / (np.pi * (d**3))) #Tension media de torsion 

#########################################################################################

#Composicion de tensiones
sa = ((saf_sc**2) + (3 * (tat_sc**2)))**(1/2) #Sigma alterno
sm = ((smf_sc**2) + (3 * (tmt_sc**2)))**(1/2) #Sigma medio