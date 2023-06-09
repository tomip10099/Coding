#Calculadora de valores de fatiga
import os

if os.name == 'nt':  
    os.system('cls') #Limpio la terminal

#Definicion de variables del elemento
Fmax = 1000 #Fuerza Maxima [Kgf]
Fmin = 500 #Fuerza Minima [Kgf]
A = 20 #Area analisis [mm2]

#Definicion del tipo de esfuerzo a la que la pieza va a estar sometida
esfuerzo = 2
# esfuerzo = 1 ---> La pieza va a estar sometida a traccion o compresion
# esfuerzo = 2 ---> La pieza va a estar sometida a flexion
# esfuerzo = 3 ---> La pieza va a estar sometida a torsion

#Variables del material
E = 205.93 #Modulo de Young de material base [GPa]
v = 0.3 #coeficiente de poisson
I = 11500 #Momento de inercia o momento de area de segundo orden [mm^4]
J = 23000 #Momento de inercia polar [mm4]
g = 9810 #Fuerza de gravedad  [mm/s^2]
Sy = 18 #Tension de fluencia [Yield Strength] 
St = 35 #Tension de rotura [Ultimate Tensile Strength]

#Definicion de variables internas
fc1 = 101.971 #Factor de conversion de GPa a Kgf/mm2
G = (E*fc1) / (2*(1+v)) #Modulo de elasticidad Transversal [kgf/mm2]

Smax = Fmax/A #Tension maxima [Kgf / mm2]
Smin = Fmin/A #Tension minima [Kgf / mm2]

Smed = ((Smax + Smin) / 2) #Tension Media [Kgf / mm2]
Samp = ((Smax - Smin) / 2) #Tension de amplitud [Kgf / mm2]
R = Smin / Smax #Relacion entre tension minima y tension maxima

def calculo_Sfa(caso):
    Sfa_ConTensiones = 0#Tension de fatiga para esfuerzos alternos simetricos en probetas de 10mm de diametro
    Se = 0
    return Se

case = 0

if (R == 1):
    case = 1 #Caso Estatico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")
    print("Tension de falla es: ", Sy, "Kgf/mm2")

elif (R == -1):
    case = 2 #Caso alterno simetrico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    if (esfuerzo == 1):
        Se = calculo_Sfa
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R == 0):
    case = 2 #Caso Pulsante
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")
    print("Tension de falla es: ", Sy, "Kgf/mm2")

