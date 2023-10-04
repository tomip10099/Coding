import numpy as np
import matplotlib.pyplot as plt 

diametro_externo_base = 80 #[mm]
diametro_interno_base = 68.3 #[mm]

diametro_externo_inserto = 68.3 #[mm]
diametro_interno_inserto = 0 #[mm]

interference = 0.06 #[mm]
friction_factor = 0.50

E_material_base = 21400 #[kg/mm2] acero
E_material_inserto = 13250 #[kg/mm2] cobre
v_material_base = 0.34 #Modulo de Poisson
v_material_inserto = 0.25

tension_fluencia_base = 20.9 #[kg/mm2] AISI 304
tension_fluencia_cobre = 6.32 #[kg/mm2] cobre

longitud_interferencia = 10 #[mm]

def interference_pressure(diametro_externo_base, diametro_interno_base, diametro_externo_inserto, diametro_interno_inserto, interference, E_material_base, E_material_inserto,v_material_base, v_material_inserto):
	
	first_term = (diametro_interno_base/E_material_base) * ((((diametro_externo_base**2) + (diametro_interno_base**2)) / ((diametro_externo_base**2) - (diametro_interno_base**2))) + v_material_base )
	second_term = (diametro_externo_inserto/E_material_inserto) * ((((diametro_externo_inserto**2) + (diametro_interno_inserto**2)) / ((diametro_externo_inserto**2) - (diametro_interno_inserto**2))) - v_material_inserto)
	p_interference = interference / (first_term + second_term)
	
	return p_interference

p_interference = interference_pressure(diametro_externo_base, diametro_interno_base, diametro_externo_inserto, diametro_interno_inserto, interference, E_material_base, E_material_inserto,v_material_base, v_material_inserto)
print("Presion de zunchado: ",round(p_interference, 3), " Kg/mm2")

def friction_force(friction_factor, p_interference, diametro_externo_inserto, longitud_interferencia):
	
	f_friction = friction_factor * (p_interference * (longitud_interferencia * np.pi * diametro_externo_inserto))
	
	return f_friction

f_friction = friction_force(friction_factor, p_interference, diametro_externo_inserto, longitud_interferencia)
print("Fuerza de friccion: ",round(f_friction, 2), " Kgf")

def transmission_torque(f_friction, diametro_externo_inserto):
	
	t_transmission = f_friction * (diametro_externo_inserto/2)
	
	return t_transmission

t_transmission = transmission_torque(f_friction, diametro_externo_inserto)
print("Torque Maximo: ",round(t_transmission, 2), " Kg.mm")

def tensiones_inserto(diametro_externo_inserto, diametro_interno_inserto, p_interference, E_material_base, v_material_inserto):
	
	tension_tangencial_inserto = -(((diametro_externo_inserto**2) * p_interference)/((diametro_externo_inserto**2)-(diametro_interno_inserto**2))) * (1 + ((diametro_interno_inserto**2)/(diametro_externo_inserto**2)))
	
	tension_radial_inserto = -(((diametro_externo_inserto**2) * p_interference)/((diametro_externo_inserto**2)-(diametro_interno_inserto**2))) * (1 - ((diametro_interno_inserto**2)/(diametro_externo_inserto**2)))
	
	desplazamiento_radial_inserto = (-((diametro_externo_inserto * p_interference) / (2 * E_material_base)) * ((((diametro_externo_inserto**2) + (diametro_interno_inserto**2))/((diametro_externo_inserto**2) - (diametro_interno_inserto**2))) + v_material_inserto))
	
	tension_corte_inserto = 0
	
	tension_axial_inserto = 0

	tension_von_misses = np.sqrt(((((tension_radial_inserto - tension_tangencial_inserto)**2)+((tension_tangencial_inserto + tension_axial_inserto)**2)+((tension_radial_inserto - tension_axial_inserto)**2))/2) + (3 * (tension_corte_inserto**2)))
	
	return tension_tangencial_inserto, tension_radial_inserto, desplazamiento_radial_inserto, tension_von_misses

tension_tangencial_inserto, tension_radial_inserto, desplazamiento_radial_inserto, tension_von_misses = tensiones_inserto(diametro_externo_inserto, diametro_interno_inserto, p_interference, E_material_base, v_material_inserto)
print("Tension tangencial inserto: ",round(tension_tangencial_inserto, 2), " Kg/mm2")
print("Tension radial inserto: ",round(tension_radial_inserto, 2), " Kg/mm2")
print("Desplazamiento radial inserto: ",np.format_float_scientific(desplazamiento_radial_inserto, 2), " mm")
print("Tension de Von Misses inserto: ",round(tension_von_misses, 2), " Kg/mm2")
