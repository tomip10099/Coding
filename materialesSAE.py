import json

#HR: Hot Rolled; Rolado en caliente
#CD: Cold Drawn; Deformado en frio ; mayor Sy y leve incremento de Su
#Su: Tensile Strength; Tension ultima, para el caso de materiales fragiles tambien se la conoce como Sut y coincide con la tension de rotura
#Sy: Yield Strength; Tension de fluencia
#Todos los valores se encuentran en kg/mm2

# Su = 3.4 Hb [Mpa] para aceros


diccionario = {
    'SAE 1006HR': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1006CD': {
        'Su': 33.65,
        'Sy': 28.55,
        'HB': 95
    },
    'SAE 1010HR': {
        'Su': 32.63,
        'Sy': 18.35,
        'HB': 95
    },
    'SAE 1010CD': {
        'Su': 37.72,
        'Sy': 30.59,
        'HB': 105
    },
    'SAE 1015HR': {
        'Su': 34.67,
        'Sy': 19.37,
        'HB': 101
    },
    'SAE 1015CD': {
        'Su': 39.76,
        'Sy': 32.63,
        'HB': 111
    }, #Hasta aca estan completos los datos.
    'SAE 1018HR': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1018CD': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1020HR': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1020CD': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1030HR': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
    'SAE 1030CD': {
        'Su': 30.60,
        'Sy': 17.33,
        'HB': 86
    },
}

with open('materialesSAE.json', 'w') as archivo:
    json.dump(diccionario, archivo)
