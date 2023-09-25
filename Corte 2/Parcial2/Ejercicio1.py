"""
Autor:  Carlos Stiven Ruiz Rojas (2259629)
        Nicolle Lopez Colonia (2259630)
Fecha: 10 de junio 2022
Descripcion: Ejercicio 1 - Parcial 2

"""

import numpy as np

ciudades= np.array(['Tulua','Florencia','Sevilla','Pradera','Bogota'])
temperaturas= np.array([20,17,45,30,15])

def obtenerdatos(ciudades,temperaturas):
    ma_temp = np.array([0])
    ma_ciudad= np.array(["                    "])
    me_temp = np.array([temperaturas[0]])
    me_ciudad= np.array([ciudades[0]])
    for i in range(0,temperaturas.size):

        if temperaturas[i] > ma_temp:
            ma_temp[0] = temperaturas[i]
            ma_ciudad[0] = ciudades[i]

        if temperaturas[i] < me_temp:
            me_temp[0] = temperaturas[i]
            me_ciudad[0] = ciudades[i]
    return f"{ma_ciudad} = {ma_temp} \n {me_ciudad} = {me_temp}"

print(obtenerdatos(ciudades,temperaturas))

