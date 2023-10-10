"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 10/10/2023
Descripcion: promedio de notas usando try - except y condicionales
"""
#Datos de entrada
nombre = input("Ingrese su nombre: ")
asignatura = input("Ingrese la asignatura: ").upper()

# En esta funcion se clasifican las notas de acuerdo a la asignatura
def clasificacion(promedio):
    if asignatura == "FUNDAMENTOS":
        if promedio >= 4.5 and promedio <= 5.0:
            clasificacion = "Excelente"
        elif promedio >= 3.8 and promedio < 4.5:
            clasificacion = "Bueno"
        elif 3 <= promedio < 3.8:
            clasificacion = "Aceptable"
        elif 2 <= promedio < 3:
            clasificacion = "Deficiente"
        elif 0 <= promedio < 2:
            clasificacion = "Malo"
        else:
            clasificacion = "Error"

    elif asignatura == "CALCULO":
        if promedio >= 4.5 and promedio <= 5.0:
            clasificacion = "Excelente"
        elif promedio >= 3.5 and promedio < 4.5:
            clasificacion = "Bueno"
        elif 3 <= promedio < 3.5:
            clasificacion = "Aceptable"
        elif 2 <= promedio < 3:
            clasificacion = "Deficiente"
        elif 0 <= promedio < 2:
            clasificacion = "Malo"
        else:
            clasificacion = "Error"

    elif asignatura == "INGLES":
        if promedio >= 4.5 and promedio <= 5.0:
            clasificacion = "Excelente"
        elif promedio >= 4 and promedio < 4.5:
            clasificacion = "Bueno"
        elif 3 <= promedio < 4:
            clasificacion = "Regular"
        elif 0 <= promedio < 3:
            clasificacion = "Malo"
        else:
            clasificacion = "Error" 

    elif asignatura == "DEPORTE":
        if promedio >= 4 and promedio <= 5.0:
            clasificacion = "Bueno"
        elif promedio >= 3 and promedio < 4:
            clasificacion = "Regular"
        elif 0 <= promedio < 3:
            clasificacion = "Malo"
        else:
            clasificacion = "Error"
    else:
        print("Ingrese una asignatura valida")
    
    return clasificacion
# En esta funcion se promedia la nota del estudiante
def promedio():
    try:

        nota1 = (float(input("Examen parcial 1: "))) * 0.20
        nota2 = float(input("Tarea 1: "))
        nota3 = ((float(input("Tarea 2: ")) + nota2)/2 ) * 0.20
        nota4 = float(input("Examen final: ")) * 0.40
        nota5 = float(input("Participacion: ")) * 0.20
        promedio = nota1+nota3+nota4+nota5
        print ("Nombre del alumno: ",nombre," \nNombre de la asignatura: ",asignatura,"\nClasificacion: ",clasificacion(promedio))
    
    except ValueError:
        print("Ingrese un dato correcto")
        promedio()

# Inica funcion
promedio()