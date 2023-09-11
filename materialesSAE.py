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
    },
    'SAE 1018HR': {
        'Su': 40.76,
        'Sy': 22.418,
        'HB': 116
    },
    'SAE 1018CD': {
        'Su': 44.836,
        'Sy': 37.703,
        'HB': 126
    },
    'SAE 1020HR': {
        'Su': 38.722,
        'Sy': 21.4,
        'HB': 111
    },
    'SAE 1020CD': {
        'Su': 47.89,
        'Sy': 39.741,
        'HB': 131
    },
    'SAE 1030HR': {
        'Su': 47.9,
        'Sy': 26.49,
        'HB': 137
    },
    'SAE 1030CD': {
        'Su': 52.988,
        'Sy': 44.83,
        'HB': 149
    },
    'SAE 1035HR': {
        'Su': 50.95,
        'Sy': 27.51,
        'HB': 143
    },
    'SAE 1035CD': {
        'Su': 56.04,
        'Sy': 46.874,
        'HB': 163
    },
    'SAE 1040HR': {
        'Su': 52.98,
        'Sy': 29.55,
        'HB': 149
    },
    'SAE 1040CD': {
        'Su': 60.121,
        'Sy': 49.93,
        'HB': 170
    },
    'SAE 1045HR': {
        'Su': 58.08,
        'Sy': 31.58,
        'HB': 163
    },
    'SAE 1045CD': {
        'Su': 64.197,
        'Sy': 54,
        'HB': 179
    },
    'SAE 1050HR': {
        'Su': 63.17,
        'Sy': 34.646,
        'HB': 179
    },
    'SAE 1050CD': {
        'Su': 70.311,
        'Sy': 59.102,
        'HB': 197
    },
    'SAE 1060HR': {
        'Su': 69.292,
        'Sy': 37.703,
        'HB': 201
    },
    'SAE 1080HR': {
        'Su': 78.463,
        'Sy': 42.798,
        'HB': 229
    },
    'SAE 1095HR': {
        'Su': 84.577,
        'Sy': 46.874,
        'HB': 248
    },
}

with open('materialesSAE.json', 'w') as archivo:
    json.dump(diccionario, archivo)
