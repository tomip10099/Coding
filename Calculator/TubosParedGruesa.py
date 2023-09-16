
ri = 2000 #Radio Interno [cm]
re = 2200 #Radio Interno [cm]
Pi = 1 #Presion Interna [Kg/cm2]
Pe = 300 #Presion Externa [Kg/cm2]

E = 1E+6 #Modulo elasticidad acero [Kg/cm2]
v = 0.3 #Coeficiente de Poisson

tr=[]
tt=[]
er=0

def tension_radial():

	tr=-(((Pi*(((re/r)**2)-1))+(Pe*((((re/ri)**2)-((re/r)**2)))))/(((re/ri)**2)-1))

	return tr

def tension_tangencial():

	tt=(((Pi*(((re/r)**2)+1))-(Pe*((((re/ri)**2)+((re/r)**2)))))/(((re/ri)**2)-1))

	return tt

