"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 8 de junio 2022
Descripcion: 

"""

import numpy as np

def cestu(n):
    estu= np.full((n),"           ")
    for i in range(0,n):
        estu[i] = input("Ingrese el nombre de los estudiantes")
    return estu


print(cestu(3))