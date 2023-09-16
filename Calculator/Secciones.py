#Archivo para calcular parametros de secciones
import numpy as np

def Circle(d):

    area = (np.pi * (d**2))/4
    second_moment_area = (np.pi * (d**4))/64
    second_polar_moment = (np.pi * (d**4))/32

    return area, second_moment_area, second_polar_moment

def Rectangle(b, h):

    area = b * h
    second_moment_area_x = (b * (h**3)) / 12
    second_moment_y = ((b**3) * h) / 12

    return area, second_moment_area_x , second_moment_y

def Hollow_circle(D, d):

    area = (np.pi * ((D - d)**2))/4
    second_moment_area = (np.pi * ((D - d)**4))/64
    second_polar_moment = (np.pi * ((D - d)**4))/32

    return area, second_moment_area, second_polar_moment