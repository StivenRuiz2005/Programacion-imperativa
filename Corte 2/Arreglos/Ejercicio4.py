"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 8 de junio 2022
Descripcion: Sema de dos arreglos

"""

import numpy as np

def suma_arr(n):
    arr1= np.zeros(n)
    arr2= np.zeros(n)
    arr_t= np.zeros(n)
    for i in range(0,n):
        arr1[i]=int(input(f"Ingrese el numero {i} del primer arreglo: "))
        arr2[i]=int(input(f"Ingrese el numero {i} del segundo arreglo arreglo: "))
        arr_t[i]= arr1[i] + arr2[i]
    return arr_t
    
n= int(input("Ingrese el tamaño de ambos arreglos "))
print(suma_arr(n))