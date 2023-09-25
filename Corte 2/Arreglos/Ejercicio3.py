"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 13 de mayo 2022
Descripcion: 

"""
import numpy as np

num2= np.array([1,2,3,4])
"""
def num_cu(num2):
    for i in range(num2.size):
        num2[i]**=2
    return num2

print(num_cu(num2))
"""
print("==========================================")

def vecinos(num2):
    for i in range(1,num2.size):
        num2[i]+=num2[i-1]
    return num2
print(vecinos(num2))