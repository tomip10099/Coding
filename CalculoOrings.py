import numpy as np

P1 = 1.4e-4
P2 = 3.5e-4
T = 120 #Segundos de leakTest
V = 1000 #Litros de la camara

P1c = P1 * 0.75
P2c = P2 * 0.75

Q = ((P1c - P2c) * V) / T #Total Leak Rate

Good_leak = 4e-5 #mbar.L/sec
small_leak = 6e-5 #mbar.L/sec
medium_leak = 9e-5 #mbar.L/sec
bad_leak = 1e-4 #mbar.L/sec

print("Leak rate: ",np.format_float_scientific(Q,2))

K_viton = 0.075
K_NBR = 0.1
coeficiente_reduccion_orings = 0.7 #El diametro de la seccion se reduce en un 30%

A_puerta = 250 * (0.8 *coeficiente_reduccion_orings)

A_tapa_resistencia = 7.24 * (5.33 * coeficiente_reduccion_orings)
A_ejes_resistencias = 0.919 * (2.62 * coeficiente_reduccion_orings)
A_resistencias = A_tapa_resistencia + A_ejes_resistencias

A_anodo_aux = 7.24 * (5.33 * coeficiente_reduccion_orings)

A_tapa_inf = 10.43 * (3.53 * coeficiente_reduccion_orings)
A_tapa_sup = 10.43 * (3.53 * coeficiente_reduccion_orings)
A_eje = 5.01 * (5.33 * coeficiente_reduccion_orings)
A_eje = A_tapa_inf + A_tapa_sup + A_eje

A_inlet_gases = 

A = A_puerta + A_resistencias + A_anodo_aux + A_eje + A_inlet_gases + A_Catodos + A_gatillos + A_visor

Qo = K * A (P1 - P2) / D #Leak rate orings