#Calculadora de tensiones dinamicas 
import os

if os.name == 'nt':  
    os.system('cls') #Limpio la terminal

#Definicion de variables del elemento
w = 0.860 #Masa del objeto [Kg]
h = 300 #altura de caida [mm]
A = 19.635 #area de la seccion resistente al impacto [mm^2]
l = 300 #Longitud de la barra [mm]

#Variables del material
E = 205.93 #Modulo de Young de material base [GPa]
v = 0.3 #coeficiente de poisson
I = 11500 #Momento de inercia o momento de area de segundo orden [mm^4]
J = 23000 #Momento de inercia polar [mm4]
g = 9810 #Fuerza de gravedad  [mm/s^2]

#Definicion de variables internas
fc1 = 101.971 #Factor de conversion de GPa a Kgf/mm2
G = (E*fc1) / (2*(1+v)) #Modulo de elasticidad Transversal [kgf/mm2]


def tension_dinamica_axial(w, h, A, l, E, fc1):

    k1 = ((E*fc1) * A)/l #Rigidez Axial de una barra

    #Tension dinamica axial
    f1 = w + (w * (( 1 + ((2 * h * k1)/w) )**(1/2)))
    sig1 = f1 / A

    print("Tension dinamica AXIAL es: ", round(sig1, 2), " kg/mm^2") 

    return f1, sig1


def tension_dinamica_flexion(w, h, A, l, E, fc1):

    k2 = ((E*fc1) * I )/l #Rigidez flexional de una barra

    #Tension dinamica en flexion
    f2 = w + (w * (( 1 + ((2 * h * k2)/w) )**(1/2)))
    sig2 = f2 / A

    print("Tension dinamica FLEXION es: ", round(sig2, 2), " kg/mm^2")

    return f2, sig2

def tension_dinamica_corte(w, h, A, l, E, fc1):

    k3 = (12 * (E*fc1) * I)/ (l**3) #Rigiez frente a un esfuerzo cortante de una barra

    #Tension dinamica cortante
    f3 = w + (w * (( 1 + ((2 * h * k3)/w) )**(1/2)))
    sig3 = f3 / A

    print("Tension dinamica CORTE es: ", round(sig3, 2), " kg/mm^2")

    return f3, sig3

def tension_dinamica_flexocortante(w, h, A, l, E, fc1):

    k4 = (6 * (E*fc1) * I)/ (l**2) #Rigiez frente a un esfuerzo flexo-cortante de una barra
    
    #Tension dinamica flexo-cortante
    f4 = w + (w * (( 1 + ((2 * h * k4)/w) )**(1/2)))
    sig4 = f4 / A

    print("Tension dinamica FLEXO-CORTANTE es: ", round(sig4, 2), " kg/mm^2")

    return f4, sig4

def tension_dinamica_torsional(w, h, A, l, G, J):

    k5 = (G * J) / l #Rigiez frente a un esfuerzo torsional de una barra

    #Tension dinamica en torsion
    f5 = w + (w * (( 1 + ((2 * h * k5)/w) )**(1/2)))
    sig5 = f5 / A 

    print("Tension dinamica TORSION es: ", round(sig5, 2), " kg/mm^2")

    return f5, sig5

def calc_all(w, h, A, l, E, fc1, G, J):

    f1, sig1 = tension_dinamica_axial(w, h, A, l, E, fc1)
    f2, sig2 = tension_dinamica_flexion(w, h, A, l, E, fc1)
    f3, sig3 = tension_dinamica_corte(w, h, A, l, E, fc1)
    f4, sig4 = tension_dinamica_flexocortante(w, h, A, l, E, fc1)
    f5, sig5 = tension_dinamica_torsional(w, h, A, l, G, J)


calc_all(w, h, A, l, E, fc1, G, J)