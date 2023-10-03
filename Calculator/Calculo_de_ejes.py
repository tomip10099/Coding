import numpy as np
import json
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

###########################################################################################################

# #Para utilizar las ecuaciones directamente del libro se deben transformar los valores de kg/mm2 a Kpsi, a cada variable anteriormente calculado se lo redefine agregando un 2
# d2 = d / 25.4 
# Se2 = Se * 1.42334 * 1000
# Su2 = Su * 1.42334 * 1000
# Sy2 = Sy * 1.42334 * 1000
# Mm2 = Mm * 55.9974
# Ma2 = Ma * 55.9974
# Tm2 = Tm * 55.9974
# Ta2 = Ta * 55.9974

# #Metodo de calculo por Goodman

# d_goodman = 25.4 * ((((16*n) / np.pi) * ((1/Se2) * (((4 * ((kf * Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2)) + (1/Su2) * (((4 * ((kf * Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2))))**(1/3))  #[mm]
# n_goodman = 1 / ((16/(np.pi * (d2**3))) * (((1/Se2) * (((4 * ((kf * Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2))) + ((1 / Su2) * (((4 * ((kf * Mm2)**2))+(3 * ((kfs * Tm2)**2)))**(1/2)))))

# #Metodo de calculo por Gerber
# A = ((4 * ((kf*Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2)
# B = ((4 * ((kf*Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2)

# d_gerber = 25.4 * ((((8 * n * A) / (np.pi * Se2)) * (1 + ((1 + (((2 * B * Se2) / (A * Su2))**2))**(1/2))))**(1/3)) # [mm]
# n_gerber = 1 / (((8 * A) / (np.pi * (d2**3) * Se2)) * (1 + ((1 + (((2 * B * Se2)/(A * Su2))**2))**(1/2))))

# #Metodo de calculo ASME-Elliptic

# d_ASME = 25.4 * ((((16*n)/np.pi) * (((4*(((kf*Ma2) / Se2)**2)) + (3 * (((kfs * Ta2) / Se2)**2)) + (4 * (((kf*Mm2) / Sy2)**2)) + (3 * (((kfs * Tm2) / Sy2)**2)))**(1/2)))**(1/3)) # [mm]
# n_ASME = 1 / ((16 / (np.pi * (d2**3))) * (((4 * (((kf*Ma2) / Se2)**2)) + (3 * (((kfs * Ta2) / Se2)**2)) + (4 * (((kf * Mm2) / Sy2)**2)) + (3 * (((kfs * Tm2) / Sy2)**2)))**(1/2)))

# #Metodo de calculo Soderberg

# d_soderberg = 25.4 * (((16 * n / np.pi) * (((1/Se2) * (((4 * ((kf*Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2))) + ((1/Sy2) * (((4 * ((kf*Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2)))))**(1/3)) # [mm]
# n_soderberg =  1 / ((16 / (np.pi * (d2**3))) * (((1/Se2) * (((4 * ((kf*Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2))) + ((1/Sy2) * (((4 * ((kf*Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2)))))

# #Calculo de tension maxima
# S_max = (((((32 * kf * (Mm2 + Ma2))/(np.pi * (d2**3)))**2) + (3 * (((16 * kfs * (Ta2 + Tm2))/(np.pi * (d2**3)))**2)))**(1/2)) * 0.000703069 #Tension maxima generada al primer ciclo de carga
# n_y = Sy / S_max #Coeficiente de seguridad de tension maxima de fluencia

def geometria(seccion, medida_representativa_1, medida_representativa_2, longitud, vel_giro):
    if seccion == "Circular":
        area, second_moment_area, second_moment_torsion = Secciones.Circle(medida_representativa_1)

    elif seccion == "Circular Hueca":
        print("seccion no desarrollada")

    elif seccion == "Cuadrada":
        print("seccion no desarrollada")
    
    elif seccion == "Cuadrada hueca":
        print("seccion no desarrollada")
    
    elif seccion == "Rectangular":
        area, second_moment_area , second_moment_torsion = Secciones.Rectangle(medida_representativa_1, medida_representativa_2)
    
    elif seccion == "Rectangular hueca":
        print("seccion no desarrollada")

    else:
        print("seccion no desarrollada")

    longitud = longitud
    vel_giro = vel_giro

    return area, second_moment_area, second_moment_torsion, longitud, vel_giro

def material(tipo_material, norma_material, codigo_material, proceso_fabricacion, check_dureza, dureza, tipo_dureza, check_tratamiento_termico, tipo_tratamiento_termico):
    
    if tipo_material == "Acero":

        if norma_material == "SAE":
            if proceso_fabricacion == "[HR] Conformado en caliente":
                proceso_fabricacion_resumido = "HR"
            else:
                proceso_fabricacion_resumido = "CD"
            

            with open("materialesSAE.json", "r") as file:
                materialesSAE = json.load(file)

                join_material = ["SAE", " ", codigo_material,proceso_fabricacion_resumido]
                material_name = "".join(join_material)

                Su = materialesSAE[material_name]["Su"] #Tension ultima
                Sy = materialesSAE[material_name]["Sy"] #Tension de fluencia
                Hb = materialesSAE[material_name]["HB"] #Dureza del material Brinell
        else:
            text = "Norma de material no cargada"
            print(text)


        if check_dureza == True:
            if tipo_dureza == "HB" and proceso_fabricacion_resumido == "HR":
                    Su = 3.4 * dureza
                    Sy = Su * 0.6
                
            elif tipo_dureza == "HB" and proceso_fabricacion_resumido == "CD":
                    Su = 3.4 * dureza
                    Sy = Su * 0.8
            else:
                print("Dureza Rockwell C no cargada")
        else:
            pass  

        if check_tratamiento_termico == True:
            pass
        else:
            pass
             
    else:
        text = "Tipo de material no cargado"
        print(text)
    
    return Su, Sy, Hb

def esfuerzos(momento_alterno_flexion, momento_medio_flexion, torsion_alterna, torsion_media, kf, kfs, medida_representativa_1, I, J):
    
    c = medida_representativa_1 / 2 #Distancia a la fibra mas alejada
    #Calculo de tensiones actuantes
    #Considero dentro del esfuerzo de flexion los esfuerzos axiales

    tension_alterna_flexion = kf * (momento_alterno_flexion * c / I ) 
    tension_media_flexion = kf * (momento_medio_flexion * c / I )

    tension_alterna_torsion = kfs * (torsion_alterna * c / J)
    tension_media_torsion = kfs * (torsion_media * c / J)

    #Composicion de tensiones por medio de Von Mises

    tension_alterna = ((tension_alterna_flexion**2) + (3 * (tension_alterna_torsion**2)))**(1/2) #Sigma alterno Von Mises
    tension_media = ((tension_media_flexion**2) + (3 * (tension_media_torsion**2)))**(1/2) #Sigma medio Von Mises

    return tension_alterna, tension_media

def diametros_minimos(Se, Su, Sy, Mm, Ma, Tm, Ta, n, kf, kfs):
    #Para utilizar las ecuaciones directamente del libro se deben transformar los valores de kg/mm2 a Kpsi, a cada variable anteriormente calculado se lo redefine agregando un 2
    Se2 = Se * 1.42334 * 1000
    Su2 = Su * 1.42334 * 1000
    Sy2 = Sy * 1.42334 * 1000
    Mm2 = Mm * 55.9974
    Ma2 = Ma * 55.9974
    Tm2 = Tm * 55.9974
    Ta2 = Ta * 55.9974
    
    #Metodo de calculo por Goodman
    d_goodman = 25.4 * ((((16*n) / np.pi) * ((1/Se2) * (((4 * ((kf * Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2)) + (1/Su2) * (((4 * ((kf * Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2))))**(1/3))  #[mm]
    
    #Metodo de calculo por Gerber
    A = ((4 * ((kf*Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2)
    B = ((4 * ((kf*Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2)
    d_gerber = 25.4 * ((((8 * n * A) / (np.pi * Se2)) * (1 + ((1 + (((2 * B * Se2) / (A * Su2))**2))**(1/2))))**(1/3)) # [mm]

    #Metodo de calculo Soderberg
    d_soderberg = 25.4 * (((16 * n / np.pi) * (((1/Se2) * (((4 * ((kf*Ma2)**2)) + (3 * ((kfs * Ta2)**2)))**(1/2))) + ((1/Sy2) * (((4 * ((kf*Mm2)**2)) + (3 * ((kfs * Tm2)**2)))**(1/2)))))**(1/3)) # [mm]

    #Metodo de calculo ASME-Elliptic
    d_ASME = 25.4 * ((((16*n)/np.pi) * (((4*(((kf*Ma2) / Se2)**2)) + (3 * (((kfs * Ta2) / Se2)**2)) + (4 * (((kf*Mm2) / Sy2)**2)) + (3 * (((kfs * Tm2) / Sy2)**2)))**(1/2)))**(1/3)) # [mm]

    return d_goodman, d_gerber, d_soderberg, d_ASME

def coeficientes_seguridad(Se, Su, Sy, tension_alterna, tension_media):
    Se2 = Se * 1.42334 * 1000
    Su2 = Su * 1.42334 * 1000
    Sy2 = Sy * 1.42334 * 1000
    tension_media2 = tension_media * 55.9974
    tension_alterna2 = tension_alterna * 55.9974

    n_soderberg = 1 / ((tension_alterna2/Se2) + (tension_media2/Sy2))
    n_goodman = 1 / ((tension_alterna2/Se2) + (tension_media2/Su2))
    n_gerber = 1 / ((tension_alterna2/Se2) + ((tension_media2/Su2)**2))
    n_ASME = 1 / (((tension_alterna2/Se2)**2) + ((tension_media2/Sy2)**2))
    n_Langer = Sy2/(tension_alterna2 + tension_media2)

    return n_soderberg,n_goodman,n_gerber,n_ASME,n_Langer
