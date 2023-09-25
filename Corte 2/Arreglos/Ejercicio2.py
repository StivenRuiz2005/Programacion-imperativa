"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 13 de mayo 2022
Descripcion: varias operaciones

"""
import numpy as np

suma_elem= np.array([1,2,3,4,5])

print("==============================================================")

def sumaa(suma_elem):
    final=0
    for suma in suma_elem:
        final += suma
    return final    

print(sumaa(suma_elem))

print("===============================================================")

def suma2(suma_elem):
    final2=0
    for suma1 in suma_elem:
        final2 += suma1**2
    return final2
print(suma2(suma_elem))

print("==============================================================")

def suma_pares(suma_elem):
    par=0
    for suma2 in suma_elem:
        if suma2 % 2==0:
            par += suma2
    return par
print(suma_pares(suma_elem))

print("==============================================================")

