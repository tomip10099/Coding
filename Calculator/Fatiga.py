#Calculadora de valores de fatiga

#Existen 3 metodos para la determinacion del ciclo de vida por fatiga
#Calculo por esfuerzo , calculo por deformacio y calculo por fractura lineal elastica

#El calculo por esfuerzo es el menos preciso, sobre todo para bajo numero de ciclos (< 10^3), pero es el mas utilizado y para grandes ciclos de fatiga es bastante preciso
#El calculo por deformacion necesita un analisis detallado de la deformacion plastica en regiones particulares, es especialmente bueno para bajo numero de ciclos
#El calculo por fractura lineal asume que ya se ah producido una grieta y ya fue detectada, y sirve para predecir el crecimiento de la grieta

#CALCULO POR ESFUERZO

def tension_fatiga(Su, rot, d):

    #Tension de fatiga de probeta de acuerdo al material
    if Su < 142:
        Se_p = 0.5 * Su
    else:
        Se_p = 71.38
    #Para valores de
    # Su < 142 kg/mm2 --> Se_p = 0.5 * Su
    # Su > 142 kg/mm2 --> Se_p = 71.38

    #Coeficiente de terminacion superficial
    #Factor de terminacion, se listan a continuacion
    ka_a = 4.51 
    # Pulido = 1.58
    # Mecanizado o forjado en frio = 4.51
    # Rolado en caliente = 57.5
    # Forjado = 272

    
    #Exponente de terminacion, se listan a continuacion
    ka_b = -0.265
    # Pulido = -0.085
    # Mecanizado o forjado en frio = -0.265
    # Rolado en caliente = -0.718
    # Forjado = -0.995
    ka = ka_a * ((Su* 9.8066)**ka_b) #Se convierte la tension ultima a Mpa al multiplicar por 9.8

    #Coefiente de tamaño para elementos rotantes
    rot = True

    #kb = 1

    #Para secciones circulares:

    #Para cargas axiales puras kb = 1

    #Para cargas de flexion o torsion, los valores se dictan a continuacion de acuerdo al diametro
    if d >= 2.79 and d <= 51:
        # 2.79 <= d <= 51 mm 
        kb = 1.24 *(d ** -0.107)

    elif d > 51 and d < 254 :
        # 51 < d <= 254 mm
        kb = 1.51 * (d ** -0.157)

    else:
        print("Error Calculating factor Kb, Diameter to big. (> 254mm)")



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
    za = 2.326 #fiabilidad deseada
    ke = 1 - (0.08*za)

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


    Se = ka * kb * kc * kd * ke * kf * Se_p #Tension de fatiga para el caso especifico

    return Se

def Caso_carga_fatiga_simple(Fmax, Fmin, Ar):

    #Definicion de caracteristicas de esfuerzos de fatiga
    #Fmax = 1000 Fuerza Maxima [Kgf]
    #Fmin = 500 Fuerza Minima [Kgf]
    #Ar = 20 Area analisis [mm2]

    Smax = Fmax/Ar #Tension maxima [Kgf / mm2]
    Smin = Fmin/Ar #Tension minima [Kgf / mm2]

    Smed = ((Smax + Smin) / 2) #Tension Media [Kgf / mm2]
    Samp = ((Smax - Smin) / 2) #Tension de amplitud [Kgf / mm2]

    return Samp,Smed

def Caso_carga_fatiga_completo(kf_flex, Smax_flex, Smin_flex, kf_ax, Smax_ax, Smin_ax, kfs, Smax_tor, Smin_tor):

    #El analisis para multiples esfuerzos aplicados simultaneamente se basa en el analisis de Von Misses para componer los esfuerzos
    #De aplicarse este metodo, en el calculo de Se , no usar el coeficiente Kc = 0.59 de torsion ya que ya lo tiene aplicado

    Smed_flex = ((Smax_flex + Smin_flex) / 2) #Tension Media [Kgf / mm2]
    Samp_flex = ((Smax_flex - Smin_flex) / 2) #Tension de amplitud [Kgf / mm2]

    Smed_ax = ((Smax_ax + Smin_ax) / 2) #Tension Media [Kgf / mm2]
    Samp_ax = ((Smax_ax - Smin_ax) / 2) #Tension de amplitud [Kgf / mm2]

    Smed_tor = ((Smax_tor + Smin_tor) / 2) #Tension Media [Kgf / mm2]
    Samp_tor = ((Smax_tor - Smin_tor) / 2) #Tension de amplitud [Kgf / mm2]
    
    Samp = (((((kf_flex * Samp_flex) + (kf_ax * (Samp_ax/0.85)))**2) + (3 * ((kfs*Samp_tor)**2)))**1/2) #Tension de amplitud [Kgf / mm2]
    Smed = (((((kf_flex * Smed_flex) + (kf_ax * Smed_ax))**2) + (3 * ((kfs*Smed_tor)**2)))**1/2)  #Tension Media [Kgf / mm2]

    Smax = Samp + Smed

    return Samp, Smed, Smax

#Criterios de falla para casos de fatiga
def Criterios_falla_fatiga(Samp, Smed, Sy, Su):

    #Ecuacion de Soderberg
        #La ecuacion de la recta que relaciona los esfuerzos, con el material y la fatiga es Samp/Se + Smed/Sy = 1
    Se_f_sod = Samp / (1 - (Smed/Sy))#Tension de fatiga de falla de soderberg

     #Ecuacion de Goodman
        #La ecuacion de la recta que relaciona los esfuerzos, con el material y la fatiga es Samp/Se + Smed/Su = 1
    Se_f_god = Samp / (1 - (Smed/Su))#Tension de fatiga de falla de Goodman

    #Ecuacion de Gerber
        #La ecuacion de la recta que relaciona los esfuerzos, con el material y la fatiga es Samp/Se + (Smed/Su)^2 = 1
    Se_f_ger = Samp / (1 - ((Smed/Su)**2))#Tension de fatiga de falla de Gerber

    #Ecuacion de ASME-elliptic
        #La ecuacion de la recta que relaciona los esfuerzos, con el material y la fatiga es (Samp/Se)^2 + (Smed/Sy)^2 = 1
    Se_f_asme = Samp / ((1 - ((Smed/Sy)**2))**1/2) #Tension de fatiga de falla de ASME-elliptic

    return Se_f_sod , Se_f_god, Se_f_ger, Se_f_asme
