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
# esfuerzo = 1 ---> La pieza va a estar sometida a traccion
# esfuerzo = 2 ---> La pieza va a estar sometida a flexion
# esfuerzo = 3 ---> La pieza va a estar sometida a torsion
# esfuerzo = 4 ---> La pieza va a estar sometida a compresion

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

def calculo_Se(case, esfuerzo, St):

    ConTen = 1 #Si ConTen = 1, evauluar factores de concentracion de tensione, si ConTen = 0, no hay concentracion de tensiones

    if (ConTen == 1):

        print("Complemento no desarrollado.")

    elif (ConTen == 0):
        
        Sfa = 0.45 * St
    
    if (esfuerzo == 1 and (case == 2 or case == 4)):
        Se = 0.7 * Sfa
    
    elif (esfuerzo == 1 and (case == 3 or case == 5)):
        Se = (0.7 * Sfa) * 1.8
    
    elif (esfuerzo == 2 and (case == 2 or case == 4)):
        Se = Sfa
    
    elif (esfuerzo == 2 and (case == 3 or case == 5)):
        Se = (0.45 * St) * 1.4
    
    elif (esfuerzo == 3 and (case == 2 or case == 4)): 
        Se = 0.58 * Sfa #Los efuerzos que se devuelven no son esfuerzos normales, son esfuerzo de corte transversal
    
    elif (esfuerzo == 3 and (case == 3 or case == 5)): 
        Se = 1.9 * (0.58 * Sfa) #Los efuerzos que se devuelven no son esfuerzos normales, son esfuerzo de corte transversal

    elif (esfuerzo == 4 and (case == 2 or case == 4)):
        Se = 0.7 * Sfa

    elif (esfuerzo == 4 and (case == 3 or case == 5)):
        Se = 1.3 * ((0.7 * Sfa) * 1.8)

    return Se

if (R == 1):
    case = 1 #Caso Estatico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")
    print("Tension de falla es: ", Sy, "Kgf/mm2")

elif (R == -1):
    case = 2 #Caso alterno simetrico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, St)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R == 0):
    case = 3 #Caso Pulsante
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, St)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R <= 0 and R >= -1):
    case = 4 #Caso Alterno asimetrico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, St)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R <= 0 and R <= 1):
    case = 5 #Caso Alterno de igual signo
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, St)
    print("Tension de falla es: ", Se, "Kgf/mm2")

else:
    print("Caso no reconocido, ingrese nuevamente los datos.")