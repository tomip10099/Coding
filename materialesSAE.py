import json

diccionario = {
    'SAE 1006HR': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1006CD': {
        'Ts': 33.65,
        'Tf': 28.55,
        'HB': 95
    },
    'SAE 1010HR': {
        'Ts': 32.63,
        'Tf': 18.35,
        'HB': 95
    },
    'SAE 1010CD': {
        'Ts': 37.72,
        'Tf': 30.59,
        'HB': 105
    },
    'SAE 1015HR': {
        'Ts': 34.67,
        'Tf': 19.37,
        'HB': 101
    },
    'SAE 1015CD': {
        'Ts': 39.76,
        'Tf': 32.63,
        'HB': 111
    }, #Hasta aca estan completos los datos.
    'SAE 1018HR': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1018CD': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1020HR': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1020CD': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1030HR': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
    'SAE 1030CD': {
        'Ts': 30.60,
        'Tf': 17.33,
        'HB': 86
    },
}

with open('materialesSAE.json', 'w') as archivo:
    json.dump(diccionario, archivo)
