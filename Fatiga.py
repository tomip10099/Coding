#Calculadora de valores de fatiga

#Existen 3 metodos para la determinacion del ciclo de vida por fatiga
#Calculo por esfuerzo , calculo por deformacio y calculo por fractura lineal elastica

#El calculo por esfuerzo es el menos preciso, sobre todo para bajo numero de ciclos (< 10^3), pero es el mas utilizado y para grandes ciclos de fatiga es bastante preciso
#El calculo por deformacion necesita un analisis detallado de la deformacion plastica en regiones particulares, es especialmente bueno para bajo numero de ciclos
#El calculo por fractura lineal asume que ya se ah producido una grieta y ya fue detectada, y sirve para predecir el crecimiento de la grieta

#CALCULO POR ESFUERZO

def tension_fatiga(Su, Sy):

    #Coeficiente de terminacion superficial
    ka = ka_a * ((Su* 9.8066)**ka_b) #Se convierte la tension ultima a Mpa al multiplicar por 9.8

    ka_a = 1 #Factor de terminacion, se listan a continuacion
    # Pulido = 1.58
    # Mecanizado o forjado en frio = 4.51
    # Rolado en caliente = 57.5
    # Forjado = 272

    ka_b = 1 #Exponente de terminacion, se listan a continuacion
    # Pulido = -0.085
    # Mecanizado o forjado en frio = -0.265
    # Rolado en caliente = -0.718
    # Forjado = -0.995


    #Coefiente de tamaño
    kb = 1

    #Para cargas axiales puras kb = 1

    #Para cargas de flexion o torsion, los valores se dictan a continuacion de acuerdo al diametro

    # 2.79 <= d <= 51 mm 
    # kb = 1.24 *(d ** -0.107)

    # 51 < d <= 254 mm
    # kb = 1.51 * (d ** -0.157)

    #en el caso de barras que no sean circulares o que solo esten sometidas a flexion (que no esten rotando) ver a continuacion
    #se emplea el calculo del diametro equivalente (de) y luego se lo reemplaza en las formulas anteriores

    # Para secciones que no estan rotando:
    # Seccion circular --> de = 0.370*d
    # Seccion Rectangular --> de = 0.808 * ((h * b)**1/2)
 
    #Coeficiente de carga
    kc = 1 #valores aproximados
    #Torsion = 0.59
    #Flexion = 1
    #Traccion / compresion = 0.85

    #Coeficiente de temperatura
    #El calculo se basa en la disminucion de la tension fluencia a diferentes temperaturas, representada como una relacion entre Sy_t/Sy = (kd)
    #Siendo Sy_t el punto de fluencia a la temperatura de operacion
    kd = 1 
    # T = 20º -- kd = 1
    # T = 50º -- kd = 1.01
    # T = 100º -- kd = 1.02
    # T = 150º -- kd = 1.025
    # T = 200º -- kd = 1.020
    # T = 250º -- kd = 1
    # T = 300º -- kd = 0.975
    # T = 350º -- kd = 0.943
    # T = 400º -- kd = 0.9
    # T = 450º -- kd = 0.843
    # T = 500º -- kd = 0.768
    # T = 550º -- kd = 0.672
    # T = 600º -- kd = 0.549


    #Coeficiente de fiabilidad, se calcula en la base al a fiabilidad del calculo y la variaciones que pueden tener los valores de tensiones de rotura (8% de desviacion estandar)
    ke = 1 - (0.08*za)
    za = 0 #fiabilidad deseada
    #Lista de fiabilidad
    # 50% -- za = 0
    # 90% -- za = 1.288
    # 95% -- za = 1.645
    # 99% -- za = 2.326
    # 99.9% -- za = 3.091
    # 99.99% -- za = 3.719
    # 99.999% -- za = 4.265
    # 99.9999% -- za = 4.753


    kf = 1 #coeficiente de miscelaneos
    #Coefiente que permite tener en consideracion algun otro factor no tabulado perteneciente al estado del material, su proceso u otros (NO ES UN COEFIENTE DE SEGURIDAD)

    Se_p = 0.5 * Su #tension de fatiga de probeta, depende del material
    #Para valores de
    # Su < 142 kg/mm2 --> Se_p = 0.5 * Su
    # Su > 142 kg/mm2 --> Se_p = 71.38

    Se = ka * kb * kc * kd * ke * kf * Se_p #Tension de fatiga para el caso especifico

    return Se

def factor_concentracion_tensiones(kt, kts, q, qs, Su): #Los valores de "kt" y "kts" se obtienen de graficos ; los valores de "q" y "qs" se obtienen de graficos de acuerdo a la resistencia del material
    # q = notch sensitivity, es decir, sensibilidad a la entalla 
    #Los factores de concentracion de tensiones son diferentes de acuerdo al tipo de esfuerzo al que se esta sometido

    kf = 1 + (q * (kt - 1)) #Factor de concentracion de tensiones reducido para esfuerzos de flexion o traccion/compresion

    kfs = 1 + (qs * (kts - 1)) #Factor de concentracion de tensiones reducido para esfuerzos de torsion (shear/corte)

    #Una manera de calcular la sensibilidad a la entalla en el caso de radios empalmes es por medio de la siguiente ecuacion
    # q = 1 / (1 + (a / (r**1/2))) donde r = al radio empalme

    # a = 0.246 - (((3.08e-3) * (Su * 1.4223))) + ((1.51e-5) * ((Su * 1.4223)**2)) - ((2.67e-8) * ((Su * 1.4223)**3)) PARA FLEXION o Traccion/Compresion
    # a = 0.190 - (((2.51e-3) * (Su * 1.4223))) + ((1.35e-5) * ((Su * 1.4223)**2)) - ((2.67e-8) * ((Su * 1.4223)**3)) PARA TORSION

    return kf, kfs














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
Su = 35 #Tension de rotura [Ultimate Tensile Strength]

#Definicion de variables internas
fc1 = 101.971 #Factor de conversion de GPa a Kgf/mm2
G = (E*fc1) / (2*(1+v)) #Modulo de elasticidad Transversal [kgf/mm2]

Smax = Fmax/A #Tension maxima [Kgf / mm2]
Smin = Fmin/A #Tension minima [Kgf / mm2]

Smed = ((Smax + Smin) / 2) #Tension Media [Kgf / mm2]
Samp = ((Smax - Smin) / 2) #Tension de amplitud [Kgf / mm2]
R = Smin / Smax #Relacion entre tension minima y tension maxima

def calculo_Se(case, esfuerzo, Su):

    ConTen = 1 #Si ConTen = 1, evauluar factores de concentracion de tensione, si ConTen = 0, no hay concentracion de tensiones

    if (ConTen == 1):

        print("Complemento no desarrollado.")

    elif (ConTen == 0):
        
        Sfa = 0.45 * Su
    
    if (esfuerzo == 1 and (case == 2 or case == 4)):
        Se = 0.7 * Sfa
    
    elif (esfuerzo == 1 and (case == 3 or case == 5)):
        Se = (0.7 * Sfa) * 1.8
    
    elif (esfuerzo == 2 and (case == 2 or case == 4)):
        Se = Sfa
    
    elif (esfuerzo == 2 and (case == 3 or case == 5)):
        Se = (0.45 * Su) * 1.4
    
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

    Se = calculo_Se(case, esfuerzo, Su)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R == 0):
    case = 3 #Caso Pulsante
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, Su)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R <= 0 and R >= -1):
    case = 4 #Caso Alterno asimetrico
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, Su)
    print("Tension de falla es: ", Se, "Kgf/mm2")

elif (R <= 0 and R <= 1):
    case = 5 #Caso Alterno de igual signo
    print("Tension de amplitud: ", Samp, "Kgf/mm2")
    print("Tension Media: ", Smed, "Kgf/mm2")

    Se = calculo_Se(case, esfuerzo, Su)
    print("Tension de falla es: ", Se, "Kgf/mm2")

else:
    print("Caso no reconocido, ingrese nuevamente los datos.")