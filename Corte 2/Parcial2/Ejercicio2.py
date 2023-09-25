"""
Autor:  Carlos Stiven Ruiz Rojas (2259629)
        Nicolle Lopez Colonia (2259630)
Fecha: 10 de junio 2022
Descripcion: Ejercicio 2 - Parcial 2

"""

import numpy as np

preg = np.array(["¿El docente explico claramente los temas?","El docente dio las calificaciones a tiempo","El docente fue respetuoso con los estudiantes"])

def evaluacion_docente(preguntas):
    promedio= np.zeros([preguntas.size])
    n= int(input("Ingrese la cantidad de estudiantes: "))
    for i in range(n):
        print("================================================")
        print(f"Estudiante {i+1}")
        print("================================================")
        for j in range(0,preguntas.size):
            promedio[j] = promedio[j] + float(input(preguntas[j]))   
    for m in range(preguntas.size):
        promedio[m]=promedio[m]/n
    
    return promedio



print(evaluacion_docente(preg))
