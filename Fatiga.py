#Calculadora de valores de fatiga
import os

if os.name == 'nt':  
    os.system('cls') #Limpio la terminal

#Definicion de variables del elemento
Fmax = 1000 #Fuerza Maxima [Kgf]
Fmin = 500 #Fuerza Minima [Kgf]
A = 20 #Area analisis [mm2]

#Variables del material
E = 205.93 #Modulo de Young de material base [GPa]
v = 0.3 #coeficiente de poisson
I = 11500 #Momento de inercia o momento de area de segundo orden [mm^4]
J = 23000 #Momento de inercia polar [mm4]
g = 9810 #Fuerza de gravedad  [mm/s^2]

#Definicion de variables internas
fc1 = 101.971 #Factor de conversion de GPa a Kgf/mm2
G = (E*fc1) / (2*(1+v)) #Modulo de elasticidad Transversal [kgf/mm2]

Smax = Fmax/A #Tension maxima [Kgf / mm2]
Smin = Fmin/A #Tension minima [Kgf / mm2]

Smed = (Smax + Smin) / 2 #Tension Media [Kgf / mm2]