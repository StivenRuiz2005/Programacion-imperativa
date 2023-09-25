"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 22 de abril 2022
Descripcion: notas

"""
print("===========================For===========================")
def notas(n_alumnos):
    p_talleres= 0
    p_parcial1= 0
    p_parcial2= 0
    p_quices= 0
    p_proyecto_final= 0
    for i in range(0,n_alumnos):
     print("========================Estudiante",i+1,"==============================")
     talleres= float(input("Digite la nota del taller: "))
     parcial1= float(input("Digite la nota del parcial 1: "))
     parcial2= float(input("Digite la nota del parcial 2: "))
     quices= float(input("Digite la nota de los quices: "))
     proyecto_final = float(input("Digite la nota del proyecto final: "))
     if 0<=parcial1<=5 and 0<=parcial2<=5 and 0<=p_talleres<=5 and 0<=p_quices<=5 and 0<=p_proyecto_final<=5:
         p_talleres= p_talleres + talleres
         p_parcial1= p_parcial1 + parcial1
         p_parcial2= p_parcial2 + parcial2
         p_quices = p_quices + quices
         p_proyecto_final = p_proyecto_final + proyecto_final
     else:
         print("Notas incorrectas")
    print("==================Promedio de todos los alumnos=========================")
    a= round(p_talleres/n_alumnos,2)
    b= round(p_parcial1/n_alumnos,2)
    c= round(p_parcial2/n_alumnos,2)
    d= round(p_quices/n_alumnos,2)
    e= round(p_proyecto_final/n_alumnos,2)
    print(f"el promedio es:\n talleres: {a}\n parcial 1:{b}\n parcial 2: {c}\n quices: {d}\n proyectos finales es:{e} ")

n_alumnos= int(input("Digite la cantidad de alumnos: "))
notas(n_alumnos)


print("===============================While=========================================")

def notas(n_alumnos1):
    global a,b,c,d,e
    p_talleres= 0
    p_parcial1= 0
    p_parcial2= 0
    p_quices= 0
    p_proyecto_final= 0
    i=0
    while (i<n_alumnos1):
         print("========================Estudiante",i+1,"==============================")
         talleres= float(input("Digite la nota del taller: "))
         parcial1= float(input("Digite la nota del parcial 1: "))
         parcial2= float(input("Digite la nota del parcial 2: "))
         quices= float(input("Digite la nota d los quices: "))
         proyecto_final = float(input("Digite la nota del proyecto final: "))
         if 0<=parcial1<=5 and 0<=parcial2<=5 and 0<=p_talleres<=5 and 0<=p_quices<=5 and 0<=p_proyecto_final<=5:
             p_talleres= p_talleres + talleres
             p_parcial1= p_parcial1 + parcial1
             p_parcial2= p_parcial2 + parcial2
             p_quices = p_quices + quices
             p_proyecto_final = p_proyecto_final + proyecto_final
         else:
             print("Notas incorrectas")
         i= i+1
    print("==================Promedio de todos los alumnos=========================")
    a= round(p_talleres/n_alumnos1,2)
    b= round(p_parcial1/n_alumnos1,2)
    c= round(p_parcial2/n_alumnos1,2)
    d= round(p_quices/n_alumnos1,2)
    e= round(p_proyecto_final/n_alumnos1,2)

n_alumnos1= int(input("Digite la cantidad de alumnos: "))
notas(n_alumnos1)
print(f"el promedio es:\n talleres: {a}\n parcial 1:{b}\n parcial 2: {c}\n quices: {d}\n proyectos finales es:{e} ")