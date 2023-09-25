"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 8 de junio 2022
Descripcion: Muestra numero mayor y menor

"""
import numpy as np

n= np.array([43,15,3,2,6,9,23,53,21,67,1,4,25,32,19,7])

def hola(n):
    mayor= np.array([0])
    menor= np.array([n[0]])
    for i in range(0,n.size):
        if n[i] > mayor:
            mayor= n[i]
        if n[i] < menor:
            menor = n[i]
    return f"El elemento menor es {menor} y el mayor es {mayor}"

print(hola(n))