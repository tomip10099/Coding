import numpy as np

#Calculo de factores de concentracion de tensiones para diferentes casos
def factores_teoricos(case, D, d, r):

    #Casos:
    # 1 = Radio empalme
    if case == 1:
        #D = Diametro mayor
        #d = Diametro menor
        #r = Radio de empalme
        
        diam_ratio = D/d
        shoul_ratio = r/d

        #Calculo de coeficiente para flexion y esfuerzo axial
        diameter_ratio = [1.02, 1.05, 1.1, 1.5, 3]
        nearest_value = None
        nearest_position = None

        for i, value in enumerate(diameter_ratio):

            if nearest_value is None or abs(value - diam_ratio) < abs(nearest_value - diam_ratio):
                nearest_value = value
                nearest_position = i

            elif abs(value - diam_ratio) == abs(nearest_value - diam_ratio) and value > nearest_value:
                nearest_value = value
                nearest_position = i

        kt_1 = [1.90, 1.70, 1.55, 1.45, 1.38, 1.35, 1.30, 1.28]
        kt_2 = [2.20, 1.80, 1.65, 1.55, 1.50, 1.40, 1.35, 1.30]
        kt_3 = [2.30, 1.85, 1.70, 1.60, 1.55, 1.45, 1.40, 1.35]
        kt_4 = [2.65, 2.10, 1.82, 1.70, 1.60, 1.55, 1.45, 1.40]
        kt_5 = [2.80, 2.30, 2.00, 1.80, 1.75, 1.70, 1.50, 1.45]

        if nearest_position == 0:
            kt_list = kt_1

        elif nearest_position == 1:
            kt_list = kt_2

        elif nearest_position == 2:
            kt_list = kt_3
        
        elif nearest_position == 3:
            kt_list = kt_4

        elif nearest_position == 4: 
            kt_list = kt_5
        
        else:
            print("Error al encontrar la posicion kt_list")

        shoulder_ratio = [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2]

        kt = np.interp(shoul_ratio, shoulder_ratio, kt_list)

        #Calculo de coeficiente para torsion
        diameter_ratio_s = [1.09, 1.20, 1.33, 2]
        nearest_value_s = None
        nearest_position_s = None

        for i, value in enumerate(diameter_ratio_s):

            if nearest_value_s is None or abs(value - diam_ratio) < abs(nearest_value_s - diam_ratio):
                nearest_value_s = value
                nearest_position_s = i

            elif abs(value - diam_ratio) == abs(nearest_value_s - diam_ratio) and value > nearest_value_s:
                nearest_value_s = value
                nearest_position_s = i

        kts_1 = [1.50, 1.30, 1.20, 1.19, 1.15, 1.10, 1.10, 1.10]
        kts_2 = [1.90, 1.60, 1.45, 1.35, 1.30, 1.25, 1.20, 1.18]
        kts_3 = [2.05, 1.70, 1.50, 1.40, 1.35, 1.30, 1.25, 1.22]
        kts_4 = [2.20, 1.75, 1.60, 1.50, 1.40, 1.35, 1.30, 1.25]

        if nearest_position_s == 0:
            kts_list = kts_1

        elif nearest_position_s == 1:
            kts_list = kts_2

        elif nearest_position_s == 2:
            kts_list = kts_3
        
        elif nearest_position_s == 3:
            kts_list = kts_4

        else:
            print("Error al encontrar la posicion kt_list")

        shoulder_ratio_s = [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2]
        
        kts = np.interp(shoul_ratio, shoulder_ratio_s, kts_list)
    
    #Caso 2 : Eje con agujero pasante
    elif case == 2:
        kt = 1
        kts = 2


    return kt, kts

def sensibilidad_entalla(r, Su):
    #los valores de "q" y "qs" se obtienen de graficos de acuerdo a la resistencia del material
    # q = notch sensitivity, es decir, sensibilidad a la entalla
    #Una manera de calcular la sensibilidad a la entalla en el caso de radios empalmes es por medio de la siguiente ecuacion

    #Calculo de sensibilidad de entalla para esfuerzos flectores y axiales
    Su_values = [ 42.184, 70.307, 105.460, 140.614]
    nearest_value = None
    nearest_position = None

    for i, value in enumerate(Su_values):

        if nearest_value is None or abs(value - Su) < abs(nearest_value - Su):
            nearest_value = value
            nearest_position = i

        elif abs(value - Su) == abs(nearest_value - Su) and value > nearest_value:
            nearest_value = value
            nearest_position = i

    q_1 = [0.58, 0.65, 0.70, 0.72, 0.75, 0.78, 0.79, 0.80]
    q_2 = [0.69, 0.75, 0.80, 0.82, 0.85, 0.86, 0.87, 0.88]
    q_3 = [0.80, 0.84, 0.89, 0.90, 0.92, 0.94, 0.95, 0.96]
    q_4 = [0.89, 0.91, 0.95, 0.96, 0.97, 0.98, 0.99, 0.99]

    if nearest_position == 0:
        q_list = q_1

    elif nearest_position == 1:
        q_list = q_2

    elif nearest_position == 2:
        q_list = q_3
    
    elif nearest_position == 3:
        q_list = q_4
    
    else:
        print("Error al encontrar la posicion q_list")

    notch_radius = [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16]

    q = np.interp(r, notch_radius, q_list)

    #Calculo de sensibilidad de entalla para esfuerzos torsores
    nearest_value = None
    nearest_position = None

    for i, value in enumerate(Su_values):

        if nearest_value is None or abs(value - Su) < abs(nearest_value - Su):
            nearest_value = value
            nearest_position = i

        elif abs(value - Su) == abs(nearest_value - Su) and value > nearest_value:
            nearest_value = value
            nearest_position = i

    qs_1 = [0.61, 0.69, 0.74, 0.78, 0.80, 0.81, 0.82, 0.83]
    qs_2 = [0.70, 0.80, 0.82, 0.84, 0.87, 0.88, 0.89, 0.90]
    qs_3 = [0.82, 0.88, 0.90, 0.91, 0.92, 0.94, 0.95, 0.96]
    qs_4 = [0.89, 0.91, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]

    if nearest_position == 0:
        qs_list = qs_1

    elif nearest_position == 1:
        qs_list = qs_2

    elif nearest_position == 2:
        qs_list = qs_3
    
    elif nearest_position == 3:
        qs_list = qs_4
    
    else:
        print("Error al encontrar la posicion q_list")

    notch_radius = [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16]

    qs = np.interp(r, notch_radius, qs_list)
     

    return q, qs

def factor_concentracion_tensiones(kt, kts, q, qs): #Los valores de "kt" y "kts" se obtienen de graficos

    #Los factores de concentracion de tensiones son diferentes de acuerdo al tipo de esfuerzo al que se esta sometido

    kf = 1 + (q * (kt - 1)) #Factor de concentracion de tensiones reducido para esfuerzos de flexion o traccion/compresion

    kfs = 1 + (qs * (kts - 1)) #Factor de concentracion de tensiones reducido para esfuerzos de torsion (shear/corte)

    return kf, kfs